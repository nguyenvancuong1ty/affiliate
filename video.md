# Tạo video avatar AI không cần lộ mặt

Trong workflow tạo video affiliate, HeyGen đảm nhận một vai trò rất cụ thể: tạo ra hình ảnh một người đang nói chuyện — mà không cần bạn thực sự lên tiếng hay lộ mặt. Kết quả là một nhân vật AI đang nói, môi khớp với giọng đọc, trông như video quay thật.

Bài này giải thích HeyGen hoạt động như thế nào để tạo ra được 1 video nhân vật AI nói chuyện, dùng nó để làm gì trong workflow của mình, và những yếu tố kỹ thuật nào ảnh hưởng đến chất lượng đầu ra.

# **Phần 1 — HeyGen hoạt động như thế nào?**

Về cơ bản, HeyGen nhận vào hai thứ: một nhân vật (avatar) và một đoạn audio. Nó phân tích audio, tính toán chuyển động môi và biểu cảm khuôn mặt tương ứng, rồi tạo ra video với nhân vật đó đang "nói" đúng theo audio.

Đây là lý do HeyGen khác với Higgsfield hay ElevenLabs — hai tool kia tạo ra hình ảnh tĩnh và audio riêng lẻ. HeyGen ghép chúng lại thành một nhân vật đang nói chuyện thật sự, với lip-sync tự động.

<aside>
💡

**Quan hệ giữa ElevenLabs và HeyGen**

HeyGen không tự tạo ra giọng nói — nó chỉ ghép avatar với audio có sẵn.

Đó là lý do trong workflow, ElevenLabs (tạo audio) phải chạy trước HeyGen.

HeyGen nhận audio từ ElevenLabs, ghép vào avatar, và xuất ra video hoàn chỉnh.

</aside>

**Hai loại avatar trong HeyGen**

HeyGen cung cấp hai loại avatar khác nhau, mỗi loại phù hợp với tình huống khác nhau:

| **Avatar có sẵn (Stock avatar)** | **Avatar tự tạo (Custom avatar)** |
| --- | --- |
| • Hàng trăm nhân vật AI được tạo sẵn bởi Heygen
• Dùng được ngay, không cần chuẩn bị
• Phù hợp để bắt đầu và test nhanh
• Không độc quyền — nhiều người khác cũng có thể dùng cùng một avatar này | • Đây là avatar do chính bạn tạo ra bằng cách upload ảnh nhân vật avatar này lên Heygen
• HeyGen học khuôn mặt và tạo ra hồ sơ nhân vật riêng
• Độc nhất — không ai có avatar giống bạn |

Trong mọi trường hợp, hãy luôn sử dụng avatar do bạn tự tạo (chính là hình ảnh nhân vật AI do bạn tạo ở bước trước bằng Higgsfield).

# **Phần 2 — Dùng HeyGen để làm gì?**

HeyGen chủ yếu được dùng cho các loại content cơ bản & an toàn, thích hợp với người mới như bạn. Những loại nội dung này yêu cầu tính ổn định cao, môi khớp với lời thoại ra và yêu cầu ít chuyển động từ nhân vật AI. Những yêu cầu này rất phù hợp với Heygen vù Heygen làm rất tốt trong việc tạo ra video trong đó nhân vật chỉ nói kèm theo một vào ngôn ngữ cơ thể đơn giản, không yêu cầu nhiều hành động phức tạp. Tuy nhiên, sau khi bạn đã làm tốt ở level cơ bản rồi thì Heygen sẽ hụt hơi hơn nhiều so với những AI nâng cao khác trong việc tạo ra những video nhiều phân cảnh chuyển động phức tạp. Phần này chúng ta sẽ bàn luận sau này, khi kỹ năng của bạn đã đủ chín nhé!

# **Phần 3 — Tư duy để video HeyGen trông tự nhiên**

Điểm yếu lớn nhất của video AI nói chung là người xem có thể nhận ra nó là AI. Với HeyGen, có 2 yếu tố kỹ thuật quyết định video trông tự nhiên hay không:

| **1** | **Chất lượng audio đầu vào quyết định chất lượng lip-sync**
HeyGen tạo chuyển động môi dựa trên audio. Audio bị rè, nhiều tạp âm, hoặc tốc độ đọc không đều sẽ cho ra lip-sync lệch và không tự nhiên. Đây là lý do cần chuẩn bị audio từ ElevenLabs thật kỹ trước khi đưa vào HeyGen. |
| --- | --- |

| **2** | **Chất lượng hình ảnh** 
Chất lượng hình ảnh nhân vật AI của bạn càng cao thì Heygen càng có nhiều dữ kiện để tạo ra những chuyển động chân thực. Nên dù bất cứ giá nào, khi tạo xong một bức ở Higgsfield, hãy luôn kiểm tra chất lượng của bức ảnh để đảm bảo video tạo ra có tính chân thực cao nhất.  |
| --- | --- |

# **Phần 4 — Những điều kỹ thuật cần biết**

Một vài điểm kỹ thuật hay gặp khi mới dùng HeyGen lần đầu:

### **Thời gian tạo video**

HeyGen cần thời gian để xử lý — thường từ vài phút đến 15–20 phút tùy độ dài audio và độ phức tạp của avatar. Đây là thời điểm tốt để chuẩn bị phần hình ảnh Higgsfield hoặc làm việc khác song song, không cần ngồi chờ.

### **Gói đăng ký Heygen**

Luôn luôn sử dụng gói Creator ($29/ tháng) của Heygen để bạn có thể sử dụng được model tạo video Avatar IV của Heygen - đây là model tạo video tốt nhất của họ. Và khi sử dụng gói trả phí, bạn có thể được tạo video từ audio với thời lượng dài hơn 3 phút → tức là video của bạn có thể dài tới 3 phút.

<aside>
💡

**Bạn vừa học được**

- HeyGen nhận audio + avatar → tạo video nhân vật đang nói với lip-sync tự động
- ElevenLabs phải chạy trước HeyGen — HeyGen không tự tạo giọng
- Chuyên Gia AI: HeyGen là hình ảnh chính. GMV Max: HeyGen là avatar phụ ở góc màn hình
- 4 yếu tố quyết định video tự nhiên: chất lượng audio, avatar phù hợp persona, background, tỷ lệ 9:16
- Lip-sync lệch → kiểm tra audio ElevenLabs trước, không phải lỗi của HeyGen
- Set tỷ lệ 9:16 ngay trong HeyGen — không để CapCut crop lại sau
</aside>


# Edit & hoàn thiện video

Sau khi đã có đủ nguyên liệu — script, hình ảnh từ Higgsfield, audio từ ElevenLabs, video avatar từ HeyGen — CapCut là nơi tất cả những thứ đó được ghép lại thành một video hoàn chỉnh.

Nếu các tool trước là nơi bạn tạo ra nguyên liệu thô, thì CapCut là bếp — nơi bạn nấu chín và trình bày. Bài này không hướng dẫn bạn làm từng bước trong một video cụ thể, mà giúp bạn hiểu giao diện CapCut, các tính năng hay dùng nhất, và một vài cài đặt quan trọng trước khi bắt đầu.

# **Phần 1 — Vai trò của CapCut trong workflow**

CapCut làm 5 việc chính trong quá trình tạo video affiliate:

- Ghép các clip lại theo thứ tự — video HeyGen, clip Higgsfield, B-roll — thành một timeline duy nhất
- Gắn audio ElevenLabs vào đúng vị trí tương ứng với hình ảnh
- Thêm caption tự động bằng tiếng Anh — đây là tính năng tiết kiệm nhiều thời gian nhất
- Xử lý các chi tiết kỹ thuật: cắt clip, chỉnh âm lượng, tăng giảm tốc độ, remove background
- Export video đúng định dạng và tỷ lệ 9:16 chuẩn TikTok

### **📌 Desktop hay điện thoại?**

CapCut có hai phiên bản: app điện thoại và phiên bản desktop (máy tính).

Với workflow tạo video affiliate, phiên bản desktop (vào capcut.com để tải capcut về máy tính) tiện hơn vì màn hình rộng hơn và thao tác trên timeline dễ hơn nhiều so với điện thoại. Tuy nhiên, nếu bạn không dành nhiều thời gian sử dụng máy tính trong ngày được thì sử dụng điện thoại hoàn toàn ổn nhé! Mình cũng dành 70% thời gian chỉnh sửa của mình trên điện thoại vì những lúc có thời gian chết thì chỉnh sửa video trên điện thoại tiết kiệm cho bạn rất nhiều thời gian.

# **Phần 2 — Giao diện CapCut — Biết mình đang nhìn vào gì**

Lần đầu mở CapCut, giao diện trông có vẻ phức tạp. Thực ra nó chỉ gồm 4 vùng chính — hiểu 4 vùng này là hiểu 80% cách dùng CapCut:

| **Preview (góc trái trên)**
Màn hình xem trước video — thứ bạn thấy ở đây là thứ sẽ xuất ra | **Media panel (góc phải trên)**
Nơi chứa tất cả file bạn đã import vào — clip, audio, ảnh |
| --- | --- |
| **Timeline (phía dưới)**
Nơi bạn sắp xếp clip theo thứ tự thời gian — đây là vùng bạn làm việc nhiều nhất | **Properties panel (góc phải)**
Cài đặt chi tiết của clip đang được chọn — âm lượng, tốc độ, hiệu ứng... |

Timeline là trung tâm của mọi thứ. Hãy hình dung nó như một bản nhạc — mỗi track là một lớp (layer): track video chính ở giữa, track audio bên dưới, track overlay phía trên. Tất cả chạy song song theo trục thời gian từ trái sang phải.

# **Phần 3 — Cài đặt trước khi bắt đầu**

### **Gói Pro — Cần những tính năng nào?**

CapCut có bản miễn phí và bản Pro. Bản miễn phí đủ để học và thực hành. Khi làm video thực tế để đăng TikTok, cần Pro để dùng 2 tính năng quan trọng:

- Auto Caption (phụ đề tự động) ở bản miễn phí sẽ có watermark logo CapCut trên video — bản Pro thì không.
- Remove Background (xóa nền) ở bản miễn phí bị giới hạn số lần dùng mỗi tháng.

Các tính năng còn lại đều dùng được ở bản miễn phí. Khi mới bắt đầu, học với bản miễn phí trước — nâng Pro khi chuẩn bị đăng video thật.

# **Phần 4 — Các tính năng hay dùng nhất**

Đây là những tính năng bạn sẽ dùng trong hầu hết mọi video. Hiểu rõ từng cái, biết khi nào cần dùng và tìm nó ở đâu trong giao diện.

### **► Thêm, xóa và sắp xếp clip**

**Dùng để làm gì:** Đưa các file video, ảnh, audio vào project và sắp xếp theo đúng thứ tự mong muốn.

**Cách dùng:** Thêm clip: kéo file từ Media panel thả vào Timeline, hoặc nhấn dấu + trên Timeline. Xóa clip: click chọn clip trên Timeline → nhấn Delete. Sắp xếp lại: giữ chuột và kéo clip sang vị trí mới trên Timeline. Duplicate: click phải vào clip → Duplicate — clip mới xuất hiện ngay sau clip gốc.

*💡 Khi kéo clip vào Timeline, CapCut thường hỏi có muốn khớp tỷ lệ với project không — chọn Keep Original để giữ nguyên, hoặc Fit to Frame nếu muốn clip tự co vào khung hình.*

### **🔊 Điều chỉnh âm lượng**

**Dùng để làm gì:** Tăng, giảm hoặc tắt tiếng của một clip cụ thể hoặc toàn bộ video — tránh trường hợp nhiều audio chạy cùng lúc nghe rối.

**Cách dùng:** Click chọn clip cần chỉnh → Properties panel bên phải → kéo thanh Volume lên/xuống. Giá trị 100 là âm lượng gốc. Kéo về 0 để tắt tiếng hoàn toàn. Nếu muốn tắt tiếng gốc của một video clip (giữ lại chỉ audio ElevenLabs): click clip → Volume → kéo về 0.

*💡 Clip HeyGen xuất ra thường có audio riêng (giọng avatar). Nếu bạn đã có audio ElevenLabs riêng, hãy tắt tiếng của clip HeyGen để tránh hai giọng chạy cùng lúc.*

### **⏩ Tăng / giảm tốc độ clip**

**Dùng để làm gì:** Thay đổi tốc độ phát lại của một clip — dùng nhiều khi muốn B-roll hình ảnh chạy nhanh hơn hoặc chậm hơn để khớp với nhịp của audio.

**Cách dùng:** Click chọn clip → Properties panel → Speed → kéo thanh hoặc nhập số thủ công. Giá trị 1x là tốc độ gốc. 2x là nhanh gấp đôi, 0.5x là chậm một nửa. CapCut sẽ tự co hoặc giãn clip trên Timeline sau khi đổi tốc độ.

*💡 Với clip HeyGen có người nói, không nên đổi tốc độ vì sẽ làm lệch lip-sync. Tính năng này chủ yếu dùng cho B-roll hình ảnh hoặc clip sản phẩm.*

### **🔲 Thêm Overlay (lớp phủ)**

**Dùng để làm gì:** Đặt một clip hoặc ảnh lên trên clip chính — dùng để chèn B-roll Higgsfield đè lên video HeyGen, hoặc đặt avatar nhỏ ở góc màn hình trong loại content GMV Max.

**Cách dùng:** Trên Timeline, nhấn nút Add Overlay (biểu tượng lớp phủ) hoặc kéo clip thả lên vùng overlay phía trên track chính. Clip overlay xuất hiện trên Preview dưới dạng một lớp riêng. Dùng chuột kéo để di chuyển vị trí, kéo góc để resize.

*💡 Overlay là cách chính để ghép video HeyGen (avatar) nhỏ vào góc màn hình khi làm GMV Max, trong khi chuỗi ảnh Higgsfield chạy ở nền.*

### **✂ Remove Background (xóa nền)**

**Dùng để làm gì:** Xóa nền của một clip hoặc ảnh để lấy chủ thể ra — dùng khi muốn đặt avatar HeyGen lên background khác, hoặc tách sản phẩm ra khỏi nền ảnh gốc.

**Cách dùng:** Click chọn clip → Properties panel → Background Removal → AI Remove Background. CapCut tự phân tích và xóa nền trong vài giây. Sau đó có thể đặt overlay lên bất kỳ background nào bạn muốn.

*💡 Tính năng này hoạt động tốt nhất khi chủ thể và nền có màu sắc tương phản rõ. Nếu nền phức tạp hoặc màu gần giống chủ thể, kết quả có thể không hoàn hảo — xem trước kỹ trước khi dùng.*

### **💬 Auto Caption (phụ đề tự động)**

**Dùng để làm gì:** CapCut nghe audio trong video và tự tạo phụ đề tiếng Anh — không cần gõ tay từng chữ. Đây là tính năng tiết kiệm thời gian nhiều nhất trong cả workflow.

**Cách dùng:** Vào menu Text → Auto Caption → chọn ngôn ngữ English → Generate. CapCut tạo caption tự động và hiển thị trên Timeline dưới dạng text track. Có thể chỉnh font, màu, cỡ chữ, vị trí trong Properties panel. Luôn đọc soát lại sau khi generate — AI đôi khi nghe sai từ, đặc biệt với tên thương hiệu.

*💡 Caption làm tăng đáng kể thời gian xem hết video — nhiều người xem TikTok không bật âm thanh. Đây là bước không nên bỏ qua.*

### **📤 Export video**

**Dùng để làm gì:** Xuất video thành phẩm ra file để đăng lên TikTok.

**Cách dùng:** Nhấn Export (góc trên phải) → chọn Resolution 1080p → Frame Rate 30fps → Format MP4 → Export. Với TikTok, 1080p 30fps MP4 là cài đặt chuẩn. Không cần xuất 4K — file nặng hơn nhưng không cải thiện chất lượng trên TikTok.

*💡 Trước khi export, xem lại preview toàn bộ video từ đầu đến cuối một lần. Dễ phát hiện những lỗi nhỏ như clip bị thừa, audio lệch, hoặc caption sai từ mà khi đang edit bạn không để ý.*

<aside>
💡

**Bạn vừa học được**

- CapCut là nơi ghép tất cả nguyên liệu lại — clip, audio, ảnh — thành video hoàn chỉnh
- 4 vùng giao diện chính: Preview, Media panel, Timeline, Properties panel
- Tạo project 9:16 ngay từ đầu — không đổi tỷ lệ sau khi đã import clip
- 6 tính năng hay dùng: thêm/xóa/duplicate clip, điều chỉnh âm lượng, tốc độ, overlay, remove background, auto caption
- Tắt âm gốc clip HeyGen khi đã có audio ElevenLabs riêng để tránh hai giọng chạy cùng lúc
- Auto caption: luôn soát lại sau khi generate — AI đôi khi nghe sai tên thương hiệu
- Export chuẩn: 1080p, 30fps, MP4 — xem preview toàn bộ trước khi export
</aside>
