#!/usr/bin/env python3
"""Transcribe an MP4 video's Vietnamese speech to a UTF-8 text file."""

from __future__ import annotations

import argparse
import os
import shutil
import site
import subprocess
import sys
import tempfile
from pathlib import Path


def configure_cuda_libraries() -> None:
    """Expose CUDA wheels installed in this virtual environment to CTranslate2."""
    library_dirs: list[str] = []
    for site_package in site.getsitepackages():
        root = Path(site_package) / "nvidia"
        for package in ("cublas", "cudnn"):
            lib_dir = root / package / "lib"
            if lib_dir.is_dir():
                library_dirs.append(str(lib_dir))

    if library_dirs:
        previous = os.environ.get("LD_LIBRARY_PATH", "")
        os.environ["LD_LIBRARY_PATH"] = ":".join(library_dirs + ([previous] if previous else []))
        if os.environ.get("STT_CUDA_LIBRARIES_CONFIGURED") != "1":
            os.environ["STT_CUDA_LIBRARIES_CONFIGURED"] = "1"
            os.execv(sys.executable, [sys.executable, *sys.argv])


configure_cuda_libraries()

from faster_whisper import WhisperModel


def extract_audio(video: Path, audio: Path) -> None:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("Khong tim thay ffmpeg trong PATH.")

    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "pcm_s16le",
            str(audio),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Chuyen giong noi trong video thanh text tieng Viet."
    )
    parser.add_argument("video", type=Path, help="Duong dan file video")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="File .txt dau ra (mac dinh: ten-video.txt)",
    )
    parser.add_argument(
        "--model",
        default="base",
        help="Whisper model: tiny, base, small, medium... (mac dinh: base)",
    )
    args = parser.parse_args()

    video = args.video.expanduser().resolve()
    if not video.is_file():
        parser.error(f"Khong tim thay video: {video}")

    output = args.output or video.with_suffix(".txt")
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="stt_") as temp_dir:
        audio = Path(temp_dir) / "audio.wav"
        extract_audio(video, audio)

        # CUDA float16 keeps inference on an NVIDIA GPU; this intentionally
        # fails on machines without an available CUDA device instead of using CPU.
        model = WhisperModel(args.model, device="cuda", compute_type="float16")
        segments, _ = model.transcribe(
            str(audio),
            language="vi",
            vad_filter=True,
            beam_size=5,
        )
        transcript = " ".join(segment.text.strip() for segment in segments).strip()

    output.write_text(transcript + "\n", encoding="utf-8")
    print(f"Da xuat transcript: {output}")


if __name__ == "__main__":
    main()
