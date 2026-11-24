# Đề thi & thể lệ MoMo Tech Contest / MoMo TechDay 2026: bản ghi chính xác từ nguồn chính thức

> Ghi chú phương pháp (đọc trước):
> - Trang `https://techday.momo.vn/topic.html` là trang rỗng, toàn bộ nội dung do JavaScript (`js/app.js`) dựng lên. Đề thi KHÔNG nằm trong HTML mà nằm trong file riêng `https://techday.momo.vn/content/exam.json`. `app.js` chỉ gọi file này sau "giờ G" (`2026-11-20T10:00:00+07:00`). File được sửa lần cuối lúc `Fri, 20 Nov 2026 03:00:48 GMT` (= 10:00:48 giờ VN 20/11/2026), tức đề được đăng đúng giờ đã hẹn.
> - Nội dung trang chủ: `content/content.json` (tiếng Việt) và `content/content.en.json` (tiếng Anh). Thể lệ chi tiết là PDF `assets/docs/the-le-cuoc-thi.pdf` (10 trang, "Phiên bản 1.0 – 13/11/2026 – Ban hành lần đầu"). Tôi đã tải và đọc toàn bộ ba nguồn này ngày 24/11/2026.
> - Theo `app.js`, đề thi chỉ có MỘT bản tiếng Việt dùng cho cả hai ngôn ngữ ("một bản tiếng Việt dùng cho cả hai ngôn ngữ"). Thể lệ Điều 37: "Nếu Thể lệ có bản dịch, bản tiếng Việt được ưu tiên áp dụng."
> - CẢNH BÁO: trên cùng máy chủ có một đề thứ hai, `content/exam-internal.json`, dành cho "Bảng nội bộ dành cho nhân viên MoMo" (trang `/internal/`). Đề này KHÔNG áp dụng cho đội sinh viên. Tôi chép lại ở mục 1 và đánh dấu rõ chỉ để tránh nhầm lẫn và làm tín hiệu tham khảo.
> - Không truy cập được: các URL `/rules.html`, `/the-le.html`, `/faq.html`, `/timeline.html`, `/agenda.html` (trả 403, nghĩa là không tồn tại trên site); form nộp bài Google Forms (401, cần đăng nhập Google). Các trang có tồn tại: `index.html`, `topic.html`, `register.html`, `regulation.html`, `submit.html`, `internal/index.html`, `internal/topic.html`.
> - Trích dẫn giữ nguyên văn, kể cả lỗi chính tả hay khoảng trắng thừa trong bản gốc (đánh dấu [sic]). Dấu `**…**` là chữ in đậm trong bản gốc.

## 1. Đề thi chính thức (topic.html) nói chính xác những gì?

### Takeaway
Đề bảng sinh viên có chủ đề lớn **"Imagine the Future Workspace (Human Centered. AI Powered)"**. Đội tự chọn đối tượng người dùng (không giới hạn). Sản phẩm phải thuộc ít nhất 1 trong 3 chủ đề **Trợ lý AI / An ninh mạng / Chống lừa đảo**. Bài nộp phải là sản phẩm thật, giám khảo dùng thử trực tuyến được, với **AI là thành phần cốt lõi**. Bài nộp gồm 4 phần: hướng dẫn sử dụng 1 trang A4 (PDF có link), mã nguồn .zip kèm README, slide tối đa 10 trang (PDF) và video tối đa 3 phút (MP4).

### Cited Findings

**1.1 Đề bài: nguyên văn khối `"id": "de-bai"`, tiêu đề "Đề bài"**: [exam.json](https://techday.momo.vn/content/exam.json), hiển thị tại [topic.html](https://techday.momo.vn/topic.html)
- Đoạn 1 (nguyên văn): "**Imagine the Future Workspace (Human Centered. AI Powered)**: Hãy tưởng tượng AI sẽ thay đổi cách đội ngũ fintech làm  việc [sic, 2 dấu cách], và qua đó thay đổi cách con người mua sắm, thanh toán, quản lý tài chính và tự bảo vệ mình trên không gian số, rồi biến ý tưởng đó thành sản phẩm dùng được ngay hôm nay." ([exam.json](https://techday.momo.vn/content/exam.json))
- Đoạn 2: "**Phạm vi người dùng**: không giới hạn. Đội tự chọn đối tượng người dùng (cá nhân, người bán, doanh nghiệp, đội vận hành…) và nêu rõ trong tài liệu mô tả." ([exam.json](https://techday.momo.vn/content/exam.json))
- Đoạn 3: "Sản phẩm ứng dụng AI phải thuộc ít nhất 01 trong 3 chủ đề: **Trợ lý AI, An ninh mạng, Chống lừa đảo**. Một sản phẩm có thể thuộc nhiều chủ đề." ([exam.json](https://techday.momo.vn/content/exam.json))
- Bảng "Chủ đề | Mô tả" (nguyên văn) ([exam.json](https://techday.momo.vn/content/exam.json)):

| Chủ đề | Mô tả (nguyên văn) |
|---|---|
| **Trợ lý AI** | "Sản phẩm hiểu nhu cầu và hành động thay người dùng, giúp họ bớt thời gian cho giúp cuộc sống trở nên tiện lợi, an toàn và thoải mái hơn." [sic] Năm nhánh con: "**Trợ lý mua sắm**: đại diện người dùng trong hành trình mua sắm trực tuyến." / "**Trợ lý cá nhân**: quản lý công việc, thời gian, thông tin cá nhân." / "**Trợ lý thanh toán**: thực hiện và quản lý giao dịch thanh toán." / "**Trợ lý bán hàng**: tư vấn, chăm sóc khách hàng và bán hàng." / "**Trợ lý tài chính**: đồng hành quản lý tài chính cá nhân." |
| **An ninh mạng** | "Sản phẩm giúp phát hiện, ngăn chặn và phản ứng với các mối đe dọa an ninh, để hệ thống và người dùng an toàn hơn. Ví dụ: hệ thống phát hiện lỗ hổng bảo mật, cảnh báo bất thường, truy vết xâm nhập… " |
| **Chống lừa đảo** | "Sản phẩm giúp người dùng nhận diện và được cảnh báo trước các hình thức lừa đảo trực tuyến, trước khi mất tiền hoặc thông tin. Ví dụ: sản phẩm giúp phát hiện tin giả, cảnh báo cuộc gọi lừa đảo,..." |

**1.2 Yêu cầu sản phẩm: khối `"id": "yeu-cau-san-pham"`**: [exam.json](https://techday.momo.vn/content/exam.json)
- "Mỗi đội cần có một sản phẩm cụ thể, sử dụng được trực tuyến, không chỉ là bản trình diễn hay bản mẫu thử."
- "**Hình thức sản phẩm**: ứng dụng, dịch vụ API, công cụ…"
- "**Dùng thử được**: Ban giám khảo truy cập và tự dùng thử sản phẩm, không phụ thuộc vào máy local của đội."
- "**AI là thành phần cốt lõi** tạo ra giá trị của sản phẩm, không chỉ là tính năng phụ."

**1.3 Thành phần bài nộp: khối `"id": "thanh-phan-bai-nop"`, bảng "Thành phần | Yêu cầu và định dạng"**: [exam.json](https://techday.momo.vn/content/exam.json)

| Thành phần | Yêu cầu và định dạng (nguyên văn) |
|---|---|
| Sản phẩm | "Tài liệu hướng dẫn sử dụng tối đa 1 trang A4, định dạng PDF chứa đường link sản phẩm để Ban giám khảo sử dụng trực tuyến được ngay, kèm tài khoản dùng thử nếu sản phẩm cần đăng nhập." |
| Mã nguồn | "Tệp nén .zip chứa toàn bộ mã nguồn. File README khai báo cách chạy, công nghệ sử dụng và danh sách Tài sản có sẵn, thư viện mã nguồn mở, công cụ AI đã dùng." |
| Tài liệu mô tả | "Bản trình chiếu (slide) tối đa 10 trang, định dạng PDF. Nêu rõ vấn đề và giải pháp của sản phẩm. Slide này được dùng cho vòng chung kết và không được sửa sau khi nộp." |
| Video giới thiệu | "Tối đa 3 phút, định dạng MP4. Quay sản phẩm đang chạy thật; phần vượt quá 3 phút sẽ không được xem." |

- Nút nộp bài: `"action": {"label": "Nộp bài", "url": "https://docs.google.com/forms/d/e/1FAIpQLSc0C4Zcc_ILiL-DEC-S5nYjgwH29vYtT9J-qAIMGe3DMcJH8A/viewform?usp=dialog"}`: [exam.json](https://techday.momo.vn/content/exam.json). Khi tải qua công cụ, form trả HTTP 401 (cần đăng nhập Google), nên tôi không xem được các trường trong form.
- Đề KHÔNG có trường "phiên bản đề", dù lịch trình trong thể lệ ghi "Công bố đề thi … Kèm phiên bản đề": [exam.json](https://techday.momo.vn/content/exam.json); [Thể lệ, Điều 14](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Tiêu đề tab của topic.html là "Exam | MoMo Tech Contest". Nhãn menu: VI "Đề thi", EN "Challenge brief": [topic.html](https://techday.momo.vn/topic.html); [content.json](https://techday.momo.vn/content/content.json); [content.en.json](https://techday.momo.vn/content/content.en.json)

**1.4 ⚠️ KHÔNG ÁP DỤNG CHO SINH VIÊN: đề "Bảng nội bộ" (exam-internal.json), chỉ để tham khảo**
- `internal/config.js` ghi: `notice: {"vi": "Bảng nội bộ dành cho nhân viên MoMo", "en": "Internal track for MoMo employees"}` và "Đề thi nội bộ nằm ở content/exam-internal.json (+ .en), tách khỏi đề bảng sinh viên". Bảng nội bộ còn có thể lệ riêng `the-le-cuoc-thi-noi-bo.pdf`: [internal/config.js](https://techday.momo.vn/internal/config.js)
- Đề nội bộ (nguyên văn, trích): "**Imagine The Future Workspace (Hình dung môi trường làm việc tương lai)**: Hãy tưởng tượng MoMo trong tương lai, nơi agent AI và con người cùng làm việc, mỗi bên đảm nhận phần việc mình làm tốt nhất…"; "**Phạm vi người dùng**: những người tham gia phát triển sản phẩm, vận hành dịch vụ và hệ thống tại MoMo."; 4 chủ đề "**Startup 1–2 người, Tăng độ tin cậy, An toàn, Tăng năng suất**". Yêu cầu riêng: "**Agent và con người cùng phối hợp**: sản phẩm thể hiện rõ phần việc agent đảm nhận và phần việc con người kiểm soát hoặc ra quyết định.": [exam-internal.json](https://techday.momo.vn/content/exam-internal.json)
- Đề nội bộ có thêm một đề tài trợ "**Đề bài tài trợ: Merchant SME 2027**", giải riêng 30.000.000 VNĐ. Bối cảnh nêu trong đề: "MoMo đang phục vụ khoảng 500.000 merchant SME, phần lớn chưa quen dùng công nghệ, bán nhiều sản phẩm qua nhiều kênh, và kỳ vọng mở rộng lên 1 triệu merchant trên cả nước." Thách thức 2027: "tăng gấp đôi quy mô, giữ chân merchant trước sự cạnh tranh của các ngân hàng, và tự nuôi được mình mà chi phí phục vụ (cost-to-serve) không tăng". Đề nêu 5 nhóm vấn đề: "Sản phẩm cho merchant SME low tech", "Năng suất bán hàng", "Năng suất chăm sóc merchant", "Rủi ro và tuân thủ" ("Phát hiện sớm gian lận, KYB"), "Merchant Trust": [exam-internal.json](https://techday.momo.vn/content/exam-internal.json)
- Ở bảng nội bộ, mã nguồn nộp qua "GitLab/Gerrit nội bộ", khác với file .zip của bảng sinh viên: [exam-internal.json](https://techday.momo.vn/content/exam-internal.json)

### Inferences
- Câu đề bài gồm hai vế. Vế 1: AI thay đổi cách **đội ngũ fintech làm việc** (đúng chủ đề "Future Workspace"). Vế 2: qua đó thay đổi cách **con người mua sắm, thanh toán, quản lý tài chính và tự bảo vệ mình trên không gian số**. Ba chủ đề bám vào vế 2: mua sắm/thanh toán/tài chính ứng với Trợ lý AI, còn "tự bảo vệ mình" ứng với An ninh mạng và Chống lừa đảo. Một bài bám sát đề có lẽ nên nói được cả hai vế: sản phẩm thay đổi cách một đội fintech (hoặc người bán, đội vận hành) làm việc, và tạo ra lợi ích cụ thể cho người dùng cuối. Đây là diễn giải của tôi, BTC không công bố.
- Định nghĩa "Trợ lý AI" dùng cụm "hiểu nhu cầu và **hành động thay người dùng**". Như vậy đề nhắm tới AI dạng agent làm việc thay người, chứ không chỉ chatbot hỏi đáp. Đây là diễn giải.
- Đề ghi "không chỉ là bản trình diễn hay bản mẫu thử" và "AI là thành phần cốt lõi". Hệ quả là một bản mockup Figma hay một app thường gắn thêm chatbot phụ có nguy cơ không đạt yêu cầu.
- Phạm vi người dùng "không giới hạn" (cá nhân, người bán, doanh nghiệp, đội vận hành…). Bắt buộc phải "nêu rõ trong tài liệu mô tả", tức trong slide.
- Đề nội bộ KHÔNG áp dụng cho sinh viên. Dù vậy, nó cho biết BTC (MoMo) đang quan tâm thật sự tới: phối hợp agent và con người, merchant SME low-tech, KYB/gian lận, cost-to-serve. Đội sinh viên nhắm đối tượng "người bán" vẫn có thể dùng các vấn đề này làm cảm hứng, nhưng không được ghi là đề chính thức của bảng sinh viên.

### Gaps
- Các trường trong form nộp bài (Google Form trả 401). Không biết form có yêu cầu chọn chủ đề, nhập mã đội hay giới hạn dung lượng file hay không. Theo trang đăng ký thì "Mã đội dùng để xác định tác giả khi nộp bài" ([content.json, registerPage](https://techday.momo.vn/content/content.json)).
- "FAQ chính thức" làm rõ đề (Điều 13) chưa được đăng tính đến 24/11/2026. Trên site chỉ có FAQ chung, không có mục làm rõ đề.

## 2. Ai được tham gia, hình thức, các vòng, hạn chót, nộp gì, giải thưởng?

### Takeaway
Cuộc thi dành cho **đội 2–3 sinh viên đại học/cao đẳng tại Việt Nam, quốc tịch Việt Nam, từ đủ 18 đến 23 tuổi**, không ai đang làm việc cho MoMo dưới bất kỳ hình thức nào, kể cả thực tập. Cuộc thi gồm vòng sơ loại online (nộp sản phẩm trước **23:59:59 ngày 03/12/2026**) và vòng chung kết trực tiếp cho **5 đội** tại TechDay **11/12/2026**, TP.HCM. Tổng giải 100 triệu đồng (50/30/20 triệu). Thành viên 3 đội đứng đầu được vào thẳng Leadership Interview của MoMo Talent 2027.

### Cited Findings

**Đối tượng tham gia**
- Điều 4 (nguyên văn): "Các thành viên là các sinh viên hiện đang theo học tại các trường đại học, cao đẳng trên toàn quốc Việt Nam, có độ tuổi từ đủ 18 đến 23 ( tính đến ngày đăng ký tham dự Cuộc thi) và mang quốc tịch Việt Nam.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 5, đối tượng không được tham gia: "Người đang làm việc cho Công ty Cổ phần Dịch vụ Di động Trực tuyến ("MoMo") hoặc bất kỳ công ty thành viên nào của MoMo, dưới bất kỳ loại hình hợp đồng nào, bao gồm: hợp đồng lao động, thử việc, thực tập (có hoặc không hưởng lương), cộng tác viên, hợp đồng dịch vụ, khoán việc." Điều kiện này "được xét trong suốt thời gian từ khi đăng ký đến hết ngày thi Techday". Danh sách còn gồm "Thành viên BTC, Ban Giám khảo" và "Người chưa đủ 18 tuổi tính tới ngày đăng ký.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Trang đăng ký thêm điều kiện: "Đội có 2 hoặc 3 thành viên, tất cả là sinh viên chưa tốt nghiệp tính đến hết ngày thi TechDay." Bản EN ghi "all undergraduate students who have not graduated as of the TechDay final date": [content.json](https://techday.momo.vn/content/content.json); [content.en.json](https://techday.momo.vn/content/content.en.json)
- Điều 6: đội "tối thiểu 02(hai) thành viên và tối đa 03(ba) thành viên". Mỗi thí sinh chỉ được ở 1 đội. Mỗi đội có 1 Trưởng nhóm đại diện. Các thành viên "tự thỏa thuận và thống nhất việc phân chia giá trị giải thưởng (nếu có) và quyền sở hữu đối với Sản phẩm dự thi": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- FAQ: "Sau khi đăng ký có được đổi hoặc thêm thành viên không?" trả lời "Không. Trưởng nhóm chỉ được chỉnh sửa thông tin đăng ký qua email trước 27/11/2026, và không được thay đổi danh tính thành viên.": [content.json](https://techday.momo.vn/content/content.json)

**Đăng ký**
- Điều 7: đăng ký tại techday.momo.vn "từ 10:00:00, 13/11/2026 đến 23:59:59, 27/11/2026". Trưởng nhóm điền tên đội và thông tin từng thành viên: "họ tên, số căn cước công dân/ số căn cước, Tỉnh/Thành phố hiện đang sinh sống, số điện thoại, email liên hệ, tên trường, chuyên ngành, năm học hiện tại (sinh viên năm thứ mấy), mã số sinh viên (MSSV)". BTC xác nhận qua email trong vòng 24 giờ: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Link form đăng ký: `https://docs.google.com/forms/d/e/1FAIpQLSeIvi48GBTcTRe8_gsFQ6y7eprhihDwzpR2L_od9PzryTDZww/viewform`: [config.js](https://techday.momo.vn/js/config.js)
- Sau khi đăng ký: "Mỗi thành viên nhận email xác nhận từ techday@mservice.com.vn kèm mã đội." và "Mã đội dùng để xác định tác giả khi nộp bài. Không chia sẻ mã cho người ngoài đội.": [content.json, registerPage](https://techday.momo.vn/content/content.json)

**Hình thức và các vòng (Điều 14, 15, 19)**: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)

| Giai đoạn | Thời gian (GMT+7), nguyên văn thể lệ |
|---|---|
| Mở đăng ký đội thi | 10:00:00, 13/11/2026 |
| Đóng đăng ký đội thi | 23:59:59, 27/11/2026 ("Không nhận hồ sơ muộn") |
| Công bố đề thi | 10:00:00, 20/11/2026 |
| Hạn gửi câu hỏi làm rõ đề | 23:59:59, 27/11/2026 (email techday@mservice.com.vn) |
| Hạn chót nộp bài | 23:59:59, 03/12/2026 ("Bài nộp sau thời điểm này không được chấm.") |
| Công bố kết quả vào vòng chung kết | Trong ngày 08/12/2026 |
| Ngày thi Vòng chung kết (Techday) | Trong ngày 11/12/2026, trực tiếp tại TP Hồ Chí Minh |
| Công bố kết quả, trao giải | Trong ngày 11/12/2026 |

- Điều 15.1: "Vòng sơ khảo: BTC sẽ chọn 05 (năm) Đội thi có kết quả tốt nhất để tham gia Vòng chung kết Cuộc thi." (Trang chủ gọi vòng này là "Vòng sơ loại 20/11 – 03/12": "Chính thức nhận đề thi chi tiết và tranh tài cùng mọi người".): [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf); [content.json](https://techday.momo.vn/content/content.json)
- Điều 15.3–15.4: đội vào chung kết phải xác nhận tham dự và "có đủ thành viên có mặt trực tiếp … để thuyết trình và trả lời câu hỏi của Ban Giám khảo". "Mọi chi phí đi lại, ăn ở … sẽ do thí sinh tự chi trả.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 19.2: "05 đội thi trình bày Sản phẩm và trả lời câu hỏi của Ban Giám khảo trực tiếp tại Techday. Nội dung thuyết trình phải dựa trên bài dự thi đã nộp trước đó.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Địa điểm chung kết: "The Adora Premium, Tân Mỹ, TP. Hồ Chí Minh", ngày "11.12.2026": [content.json](https://techday.momo.vn/content/content.json)

**Nộp bài (Điều 10)**: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Mỗi đội "chỉ được ghi nhận 01 (một) bài dự thi hợp lệ duy nhất". Nếu nộp nhiều lần, "BTC chỉ chấm bài thi được nộp gần nhất trước thời điểm kết thúc hạn nộp bài".
- Đội "phải đảm bảo BTC có thể truy cập, kiểm tra và sử dụng Sản phẩm và duy trì khả năng truy cập và hoạt động của các Sản phẩm này đến hết ngày thi Techday". FAQ ghi rõ: "Đến hết ngày thi TechDay (11/12/2026)" ([content.json](https://techday.momo.vn/content/content.json)).
- Sau hạn chót, đội không được "chỉnh sửa, thay thế, bổ sung hoặc cập nhật bài thi đã nộp". Điều 31.4 cấm "cập nhật Sản phẩm đang chạy tại đường link đã nộp, sau hạn chót".

**Giải thưởng (Điều 23–25)**
- Giải Nhất 50.000.000, Giải Nhì 30.000.000, Giải Ba 20.000.000 VNĐ, mỗi giải 1 đội, "đã bao gồm thuế". Tiền được chuyển khoản vào tài khoản của Trưởng nhóm sau khi khấu trừ thuế TNCN tại nguồn: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Quyền lợi kèm theo: "Top 3 được vào thẳng vòng Leadership Interview" của MoMo Talent 2027. FAQ: "Thành viên của 3 đội đứng đầu được miễn các vòng Application & CV Screen, Cognitive Test và Technical Assessment, vào thẳng vòng Leadership Interview (dự kiến 04/01 – 24/01/2027, lịch có thể thay đổi). Quyết định tuyển dụng cuối cùng được đưa ra tại vòng này.": [content.json](https://techday.momo.vn/content/content.json)
- Điều 34.3: "Việc tham gia Cuộc thi hoặc nhận giải không hình thành quan hệ lao động và không phải là lời mời làm việc hay thực tập tại MoMo.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Bối cảnh MoMo Talent 2027: chương trình 6 tháng, dành cho "final-year students and graduates with under 2 years of experience", làm full-time từ 02/2027. Các vị trí gồm Trainee Product Management (AI Products), Machine Learning Engineering, AI Engineering, Security Engineering, App Security Engineering, Network Engineering: [momo.careers/momo-talent](https://momo.careers/momo-talent)

### Inferences
- Lịch thực tế cho việc xây sản phẩm là khoảng **13,5 ngày**, từ 10:00 20/11 đến 23:59 03/12. Tính từ hôm nay (24/11) còn khoảng 9,5 ngày.
- Sản phẩm phải chạy ổn định trên một link công khai liên tục **từ 03/12 đến hết 11/12**, và không được deploy lại sau 03/12. Đội cần hạ tầng ổn định (tránh free tier tự ngủ, tránh API key hết quota) và không được vá lỗi trên production sau hạn chót.
- Slide nộp lúc sơ loại cũng chính là slide dùng ở chung kết ("không được sửa sau khi nộp"). Vì vậy slide cần làm sẵn ở mức chất lượng chung kết ngay từ đầu.

### Gaps
- Không có thông tin về hình thức chung kết như số phút thuyết trình hay Q&A: BTC chưa công bố.
- Không có giải phụ hay giải khuyến khích cho bảng sinh viên. Giải tài trợ 30 triệu Merchant SME chỉ có trong đề nội bộ.

## 3. Tiêu chí chấm chính thức, trọng số và Ban Giám khảo

### Takeaway
Thể lệ công bố **3 tiêu chí: Sáng tạo; Chất lượng & mức độ hoàn thiện; Tiềm năng tác động**. **Trọng số không được công bố.** Mỗi bài vòng sơ loại được ít nhất 3 giám khảo chấm độc lập. Ban Giám khảo gồm 7 người, đều là lãnh đạo hoặc chuyên gia công nghệ, AI của MoMo.

### Cited Findings
- Điều 18, bảng tiêu chí (nguyên văn): [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)

| Tiêu chí | Nội dung đánh giá (nguyên văn) |
|---|---|
| Sáng tạo | "Ý tưởng mới, có tính đột phá hoặc cách tiếp cận khác biệt so với các giải pháp hiện có." |
| Chất lượng & mức độ hoàn thiện | "Sản phẩm tại thời điểm nộp bài: vận hành ổn định, người dùng có thể trải nghiệm trực tiếp, hoàn thiện về tính năng và trải nghiệm." |
| Tiềm năng tác động | "Giá trị khi được triển khai trong tương lai: khả năng mở rộng trên quy mô lớn và số lượng người dùng có thể hưởng lợi." |

- Về trọng số, thể lệ chỉ ghi: "Cách tính điểm chi tiết do Ban Giám khảo thống nhất trước khi chấm và được áp dụng như nhau cho tất cả bài dự thi.". Như vậy **trọng số hay thang điểm: không công bố**: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 19.1: "mỗi bài được ít nhất 03 giám khảo chấm độc lập và 05 đội có điểm cao nhất vào vòng chung kết." Điều 20: nếu bằng điểm, "Trưởng Ban Giám khảo quyết định và ghi lý do vào biên bản". Điều 32.1: "BTC không tiếp nhận khiếu nại hoặc yêu cầu phúc khảo liên quan đến điểm số…": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 21: "Ban Giám khảo: gồm 7 người". Danh sách công bố trên site (mục "Ban giám khảo") ([content.json](https://techday.momo.vn/content/content.json)):
  1. Thái Trí Hùng, "Chief Technology Officer, MoMo"
  2. Hồng Trung Dũng, "Head of AI & Data, MoMo"
  3. Nguyễn Tiến Huy, "Manager - Research Scientist, MoMo"
  4. Nguyễn Đăng Phước, "Sr. Manager - Software Engineering, MoMo"
  5. Lê Ngọc Thạch, "Sr. Lead - AI Engineering, MoMo"
  6. Nguyễn Tiến Đạt, "Head of ITC Hanoi, MoMo"
  7. Phạm Thành Trí, "Manager - AI Engineering, MoMo"
- Lưu ý về chức danh: mục "Chia sẻ" trên site ghi Tăng Thị Hà Yên là "Head of AI & Data, MoMo", trùng chức danh với giám khảo Hồng Trung Dũng. Site tự không nhất quán ở điểm này, tôi không xác minh được ai giữ chức danh hiện tại: [content.json](https://techday.momo.vn/content/content.json)

### Inferences
- Ban Giám khảo nghiêng hẳn về kỹ thuật: CTO, AI/Data, Research Scientist, AI Engineering, Software Engineering, không có giám khảo kinh doanh hay marketing. Do đó chất lượng kỹ thuật thật của phần AI (kiến trúc, độ ổn định, đánh giá mô hình) có khả năng bị soi kỹ, hơn là chỉ pitch đẹp.
- Tiêu chí "Chất lượng & mức độ hoàn thiện" được chấm trên "Sản phẩm tại thời điểm nộp bài", nên giám khảo sẽ tự dùng thử link. Một sản phẩm hẹp nhưng chạy mượt có lẽ lợi hơn một sản phẩm rộng mà lỗi.
- Tiêu chí "Tiềm năng tác động" nhấn vào "mở rộng trên quy mô lớn" và "số lượng người dùng có thể hưởng lợi". Slide nên định lượng được quy mô bài toán, ví dụ số người dùng hay số giao dịch bị ảnh hưởng.

### Gaps
- Trọng số, thang điểm, rubric chi tiết: không công bố.
- Không rõ tiêu chí ở vòng chung kết có giống vòng sơ loại không. Thể lệ chỉ có một bảng tiêu chí chung cho "bài dự thi".

## 4. Ràng buộc kỹ thuật, tài nguyên được cung cấp, sở hữu trí tuệ, tính nguyên bản, mô hình bên thứ ba

### Takeaway
Đề **không giới hạn** ngôn ngữ lập trình hay mô hình AI. Theo thể lệ, đội được dùng thư viện, dataset, mô hình, mã nguồn có sẵn nếu có quyền sử dụng hợp pháp. **Không có API, dữ liệu, sandbox hay cloud credit nào của MoMo được công bố** cho bảng sinh viên. Đội giữ quyền sở hữu bài thi, nhưng cấp cho MoMo quyền sử dụng không độc quyền, miễn phí, vô thời hạn. Đội không được nộp sản phẩm đã làm từ trước cho chính bài toán này, và phải khai báo "Tài sản có sẵn" cùng công cụ AI đã dùng trong README.

### Cited Findings
- Điều 12.1: "Ngôn ngữ lập trình và mô hình AI được phép hoặc bị giới hạn (nếu có) do đề thi quy định." Đề thi (exam.json) **không** nêu giới hạn nào: [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf); [exam.json](https://techday.momo.vn/content/exam.json)
- Điều 12.2: "Trừ khi đề thi quy định khác, đội thi được sử dụng thư viện, công cụ, bộ dữ liệu (dataset), mô hình và mã nguồn có sẵn để hỗ trợ xây dựng Sản phẩm, với điều kiện đội có quyền sử dụng hợp pháp theo giấy phép hoặc điều khoản sử dụng của chúng.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 12.4: "Dữ liệu cá nhân hoặc dữ liệu của doanh nghiệp được dùng trong Sản phẩm phải được ghi rõ trong README … gồm nguồn dữ liệu, phạm vi sử dụng và căn cứ được phép sử dụng (dữ liệu công khai, có giấy phép, có sự đồng ý hoặc đã ẩn danh hóa).": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 12.5: "Đội thi không được nộp Sản phẩm đã phát triển trước Cuộc thi cho chính bài toán của đề. Tài nguyên có sẵn dùng làm nền tảng phải được khai báo là Tài sản có sẵn." Điều 28.1: phần nào không được liệt kê trong README thì "được suy đoán là tạo ra trong thời gian Cuộc thi". Điều 31.7 cấm "Cố ý che giấu việc sử dụng Tài sản có sẵn.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 11: tài nguyên do BTC cung cấp "(nếu có) … như dữ liệu, API, tài khoản dịch vụ hoặc tài liệu tham khảo, cùng phạm vi và điều kiện sử dụng sẽ được nêu trong đề thi hoặc FAQ chính thức". Đề thi hiện **không liệt kê tài nguyên nào**. Với tài nguyên tự chuẩn bị, "đội tự chịu chi phí": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf); [exam.json](https://techday.momo.vn/content/exam.json)
- Điều 28.2 có nhắc ví dụ "tài khoản dịch vụ đám mây (AWS, Google Cloud…), API, dữ liệu, phần mềm và công cụ do BTC cung cấp" kèm điều kiện sử dụng. Đây là điều khoản khung, không phải cam kết cấp tài nguyên. Nhà tài trợ trên site: "Amazon Web Services" và "G-Asia Pacific": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf); [content.json](https://techday.momo.vn/content/content.json)
- Điều 28.4: "Đội thi phải khai báo công cụ AI đã dùng khi được yêu cầu và chịu trách nhiệm nêu [sic] nội dung do AI tạo ra vi phạm quyền của bên thứ ba." Đề cũng yêu cầu README liệt kê "công cụ AI đã dùng": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf); [exam.json](https://techday.momo.vn/content/exam.json)
- Điều 27: "Bài dự thi thuộc quyền sở hữu của các thành viên Đội thi … không làm chuyển giao quyền sở hữu Bài dự thi cho BTC". Đồng thời đội cấp cho BTC "quyền sử dụng không độc quyền, miễn phí và không giới hạn thời gian … cho mục đích nghiên cứu, quảng bá, giáo dục và truyền thông liên quan đến Cuộc thi": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 28.6–28.7: không chia sẻ mã nguồn với đội khác trong thời gian thi. BTC "khuyến khích" công khai mã nguồn mở sau cuộc thi. "BTC hoặc đội thi khác có thể đang phát triển ý tưởng tương tự một cách độc lập; việc này không bị xem là xâm phạm quyền của Đội thi.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Điều 31, các hành vi bị cấm, gồm: "Người ngoài đội trực tiếp tham gia xây dựng Sản phẩm"; "Tấn công, khai thác lỗ hổng hệ thống của BTC hoặc đội khác": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)

### Inferences
- Không có API hay dữ liệu MoMo, nên đội phải tự giả lập dữ liệu (dữ liệu tổng hợp hoặc công khai) và tự tích hợp LLM/API bên thứ ba bằng chi phí của mình. Sản phẩm có thể là sản phẩm độc lập, không bắt buộc chạy trong app MoMo. Đề không yêu cầu mini-app MoMo.
- Với chủ đề An ninh mạng: Điều 31.5 cấm tấn công hệ thống của BTC. Demo kiểu quét lỗ hổng nên chạy trên mục tiêu do đội tự dựng.
- Dùng LLM thương mại (OpenAI, Claude, Gemini…) không bị cấm, nhưng phải khai báo trong README và tuân thủ điều khoản của nhà cung cấp.

### Gaps
- Không có thông tin cloud credit từ AWS hay nhà tài trợ cho thí sinh: không công bố.
- Chưa có "FAQ chính thức" về tài nguyên (hạn hỏi là 27/11/2026).

## 5. Tinh thần của đề: BTC coi trọng điều gì?

### Takeaway
Thông điệp lặp lại khắp site là **"Human centered ✦ AI powered"**: hiểu con người sâu sắc để đặt đúng bài toán, rồi dùng AI làm lõi giải pháp. Kèm theo đó là yêu cầu **sản phẩm thật, dùng được ngay hôm nay** cho **bài toán thật**, và mục đích thể lệ nêu rõ về **cách làm việc hiệu quả giữa con người và AI trong tương lai**.

### Cited Findings
- Giới thiệu TechDay 2026 (nguyên văn): "MoMo đã & đang kết hợp công nghệ (AI) và sự thấu hiểu (con người) để đưa ra các sản phẩm công nghệ phục vụ hàng triệu người dùng. AI powerful, nhưng thiếu sự thấu hiểu và đồng cảm của con người để định hướng thì cũng không thể làm thành giải pháp thực tế. Nghệ thuật là kết hợp được cả hai.": [content.json](https://techday.momo.vn/content/content.json)
- Slogan: "Human centered ✦ AI powered". Mô tả site: "đội 2–3 người xây sản phẩm AI dùng được thật": [content.json](https://techday.momo.vn/content/content.json)
- Giới thiệu Tech Contest: "Cuộc thi AI cho sinh viên Việt Nam: đội 2–3 người xây giải pháp AI lấy con người làm trọng tâm, giải bài toán thật của người dùng MoMo." Bản EN: "build human-centered AI solutions to real problems of MoMo users": [content.json](https://techday.momo.vn/content/content.json); [content.en.json](https://techday.momo.vn/content/content.en.json)
- Thể lệ, Điều 3 "Mục đích": "Tạo không gian chia sẻ và trao đổi của đội ngũ công nghệ MoMo và những bạn trẻ yêu thích công nghệ. Phát triển những ý tưởng mới để cùng nhau xây dựng cách làm việc hiệu quả giữa con người và AI trong tương lai.": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Các câu nói của lãnh đạo MoMo trong mục "Chia sẻ về cuộc thi & AI" (nguyên văn) ([content.json](https://techday.momo.vn/content/content.json)):
  - Nguyễn Mạnh Tường (CEO): "Hiểu con người để đặt đúng bài toán: việc hiểu người dùng một cách sâu sắc để xác định đúng vấn đề cần giải quyết."
  - Thái Trí Hùng (CTO, giám khảo): "Dẫn dắt AI, đừng để AI dẫn dắt mình. Đó là cách chúng ta tạo nên làn sóng mới."
  - Tăng Thị Hà Yên (Head of AI & Data): "… chỉ khi bắt tay vào làm, chúng ta mới tạo ra kết quả. Và khi thực sự làm chủ, theo đuổi công việc đến cùng, chúng ta mới có thể tạo nên những sản phẩm có giá trị…"
  - Trần Nhơn Nghĩa (Senior Manager - Data): "Khi ai cũng có AI, lợi thế không còn nằm ở công cụ. Nó thuộc về người đủ nhanh để đi trước và đủ tỉnh để không đi lạc."
  - Lê Ngọc Thạch (Sr. Lead AI Engineering, giám khảo): "MoMo Tech Contest 2026 là cơ hội để bạn biến ý tưởng táo bạo thành sản phẩm thật…"
  - Tiền Uy Doãn (Trainee - Data): "Đừng tin AI. Hãy tin bản thân."
- Bối cảnh: MoMo đã triển khai công cụ chống lừa đảo dùng AI, gồm hệ thống cảnh báo giao dịch bất thường phân tích "hàng trăm biến số hành vi", mô hình AI gắn nhãn tài khoản xanh/vàng/đỏ, và sinh trắc học kết hợp iProov "Dynamic Liveness". Các công cụ này được trưng bày tại "Sinh viên với An ninh mạng 2025" (bài đăng 18/11/2025): [SGGP](https://www.sggp.org.vn/momo-gop-phan-huong-toi-khong-gian-tai-chinh-so-an-toan-post824133.html)

### Inferences
- Câu chuyện bài thi nên bắt đầu từ một người dùng cụ thể và một vấn đề được hiểu sâu (human centered), cho thấy AI làm phần việc lõi (AI powered). Nếu sát với tinh thần "Future Workspace", bài thi cũng nên chỉ rõ phần nào AI làm, phần nào con người kiểm soát hoặc quyết định. Đề bảng sinh viên KHÔNG bắt buộc điều này. Đó là yêu cầu của đề nội bộ, nhưng nó cho thấy tư duy của BTC.
- Có một độ vênh nhỏ giữa câu giới thiệu "giải bài toán thật của người dùng MoMo" (trang chủ) và đề thi "Phạm vi người dùng: không giới hạn". Đề thi là văn bản cụ thể hơn và được công bố sau. Tuy vậy, chọn bài toán gắn với hệ sinh thái MoMo (ví ví điện tử, thanh toán, người bán, chống lừa đảo trên ví) có lẽ giúp bài thi được giám khảo đánh giá là "thật" và có "tiềm năng tác động". Đây là diễn giải.
- Chủ đề Chống lừa đảo và An ninh mạng trùng với mảng MoMo đã có sản phẩm (cảnh báo giao dịch, nhãn tài khoản, sinh trắc học). Vì vậy tiêu chí "Sáng tạo … khác biệt so với các giải pháp hiện có" sẽ khó hơn ở mảng này: đội cần một góc tiếp cận chưa có, không lặp lại thứ MoMo đã làm.

### Gaps
- BTC không công bố ưu tiên giữa 3 chủ đề, hay ưu tiên đối tượng người dùng nào.

## 6. Các mùa trước và chương trình liên quan của MoMo

### Takeaway
**Không tìm thấy nguồn đáng tin nào về một mùa "MoMo TechDay" hay "MoMo Tech Contest" công khai trước 2026**, dù site gọi đây là "chuỗi sự kiện công nghệ hằng năm". Tiền lệ gần nhất tìm được là **Generative AI Hackathon 2023** (16/8–03/10/2023) của MoMo, nhưng không rõ đối tượng dự thi và đội thắng.

### Cited Findings
- Site mô tả: "Chuỗi sự kiện công nghệ hằng năm của MoMo dành cho bạn trẻ: cuộc thi MoMo Tech Contest, ngày hội MoMo TechDay và sự kiện tuyển dụng MoMo Talent.": [content.json](https://techday.momo.vn/content/content.json)
- [Mùa 2023] "Generative AI Hackathon 2023 – Ai cũng có thể "xài" AI": diễn ra từ 16/8/2023 đến 03/10/2023, gồm ba vòng Sơ Loại, Thuyết Trình và Chung Kết, chung kết ngày 03/10 tại Tầng 6, Phú Mỹ Hưng Tower (TP.HCM). Thông tin lấy từ đoạn trích kết quả tìm kiếm của trang [momo.careers](https://momo.careers/generative-ai-hackathon-2023-ai-cung-co-the-xai-ai). Khi tải trực tiếp, URL này trả về trang danh sách bài "Life At MoMo" (sự kiện nội bộ), nên tôi **không xác minh trực tiếp** được nội dung, đối tượng (nội bộ hay sinh viên), đội thắng hay nhận xét của giám khảo.
- [2025] MoMo đồng hành cùng Cục An ninh mạng tại cuộc thi "Sinh viên với An ninh mạng 2025" (do Bộ Công an tổ chức, không phải cuộc thi của MoMo). Chung khảo ngày 15/11/2025 tại Hà Nội, khoảng 200 đội: [SGGP](https://www.sggp.org.vn/momo-gop-phan-huong-toi-khong-gian-tai-chinh-so-an-toan-post824133.html)
- Kết quả tìm kiếm "MoMo Hackathon" chủ yếu ra các cuộc thi của **MTN MoMo (châu Phi)**, một công ty khác hoàn toàn, không liên quan đến MoMo Việt Nam. Cần tránh nhầm khi tìm thêm: ví dụ [MoMo Hackathon 2026 South Africa](https://momodevelopercommunity.mtn.com/events/momo-hackathon-2026-south-africa-16).

### Inferences
- Rất có thể 2026 là mùa đầu tiên của MoMo Tech Contest công khai cho sinh viên, với dạng "Tech Series" gồm Contest + TechDay + Talent. Tôi không có bằng chứng phủ định, nhưng cũng không tìm thấy mùa trước. Do đó không có "đội thắng mùa trước" để tham khảo.

### Gaps
- Đội thắng và những gì giám khảo khen ở các cuộc thi trước của MoMo: không tìm thấy nguồn.
- Không tìm thấy bài báo VnExpress, Tuổi Trẻ, Thanh Niên, CafeBiz, ICTNews, Genk, VietnamNet hay Dân trí nào về "MoMo Tech Contest 2026" hay "MoMo TechDay 2026" tính đến 24/11/2026, qua công cụ tìm kiếm tôi dùng (chỉ tìm được kết quả ở Mỹ).

## 7. Năm tổ chức và giai đoạn hiện tại (tính đến 24/11/2026)

### Takeaway
Đây là **mùa 2026**, đã xác nhận. Tính đến **24/11/2026**: đề đã công bố (20/11, 10:00), **đăng ký vẫn mở đến 23:59:59 ngày 27/11/2026**, hạn gửi câu hỏi làm rõ đề cũng là 27/11. Vòng sơ loại đang diễn ra, **hạn nộp bài 23:59:59 ngày 03/12/2026**.

### Cited Findings
- Tiêu đề site: "MoMo TechDay 2026 | Imagine The Future Workspace". Meta: "MoMo TechDay 2026, 11.12.2026 at THE ADORA PREMIUM, Tan My, Ho Chi Minh City.": [techday.momo.vn](https://techday.momo.vn/)
- Thể lệ phiên bản 1.0, ban hành 13/11/2026, hiệu lực "từ ngày 13/11/2026 đến khi hoàn tất trao giải và giải quyết xong khiếu nại": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)
- Đề thi được đưa lên máy chủ lúc 10:00:48 giờ VN ngày 20/11/2026, theo header `last-modified: Fri, 20 Nov 2026 03:00:48 GMT` của [exam.json](https://techday.momo.vn/content/exam.json). `content.json` được sửa lần cuối lúc `Fri, 20 Nov 2026 09:52:04 GMT`.
- Đếm ngược đăng ký trên trang chủ: `"deadline": "2026-11-27T23:59:59+07:00"`, nhãn "Còn {n} ngày · hạn đăng ký 27/11": [content.json](https://techday.momo.vn/content/content.json)
- Đăng ký tham dự ngày hội TechDay (khách tham quan) vẫn ở trạng thái "Sắp mở đăng ký" (`url` rỗng): [content.json](https://techday.momo.vn/content/content.json)
- Liên hệ chính thức duy nhất: website techday.momo.vn và email techday@mservice.com.vn. Điều 16.5: yêu cầu gửi qua kênh khác "không có giá trị ràng buộc": [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)

### Inferences
- Nếu đội chưa đăng ký thì phải đăng ký trước 23:59:59 ngày 27/11. Câu hỏi làm rõ đề (ví dụ có tài nguyên hay credit không, có giới hạn mô hình không) cũng phải gửi email trước mốc đó.

### Gaps
- Chưa có thông tin về đăng ký tham dự TechDay cho khách, agenda chi tiết, thời lượng thuyết trình ở chung kết.
