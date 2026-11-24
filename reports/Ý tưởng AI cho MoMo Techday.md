# Đặt cược vào trợ lý thuế cho hộ kinh doanh

Ý tưởng đáng đầu tư nhất cho một đội sinh viên ở MoMo Tech Contest 2026 là **"Sổ Sẵn"**. Đây là trợ lý AI dùng giọng nói, giúp hộ kinh doanh tự ghi sổ, canh ngưỡng doanh thu 1 tỷ đồng và hiểu nghĩa vụ thuế mới dựa trên chính dòng tiền của họ. Đi kèm là một "bàn làm việc chính sách": AI đọc văn bản luật mới và đề xuất thay đổi quy tắc, nhân viên vận hành duyệt. Ý tưởng này hội đủ những gì đề thi và hội đồng giám khảo đòi hỏi:
- **Nỗi đau có số liệu độc lập mạnh:** chỉ **13,9%** hộ hiểu rõ quy định thuế áp dụng từ 2026, và **73,3%** coi thủ tục pháp lý là trở ngại lớn nhất.
- **Quy mô lớn:** cả nước có khoảng **6,1 triệu hộ**, trong đó **hơn 500.000** điểm bán dùng MoMo QR.
- **Thời điểm gấp:** chu kỳ khai năm đầu tiên sau khi bỏ thuế khoán kết thúc **31/01/2027**, ngay sau chung kết.
- **Ít trùng với AI MoMo đang chạy:** chấm điểm gian lận, nhãn người nhận, eKYC, chấm điểm tín dụng và Moni đều không đụng tới bài toán này.
- **Làm được trong 9 ngày:** dữ liệu giả lập cộng văn bản luật công khai là đủ để AI tạo giá trị thật.

Phương án dự phòng là **"30 Phút Vàng"**, trợ lý phản ứng sau lừa đảo cho cả nạn nhân lẫn chuyên viên chống gian lận. Đây là ý tưởng sáng tạo nhất và đánh thẳng vào giới hạn mà chính MoMo thừa nhận. Điểm yếu là tác động khó chứng minh, và ý tưởng hơi lệch định nghĩa "Chống lừa đảo" của đề (đề nhấn vào việc cảnh báo *trước khi* mất tiền). Một số hướng phổ biến nên tránh vì MoMo đã có hoặc vì đội không có dữ liệu để làm thật: cảnh báo trước khi chuyển tiền, gắn nhãn tài khoản nhận, phát hiện tài khoản trung gian nhận tiền lừa đảo (money mule), giải thích điểm tín dụng, nhắc gia hạn tự động. Rủi ro lớn nhất của Sổ Sẵn nằm ở hai chỗ: AI trích sai điều luật, và hạ tầng phải chạy không đổi từ 03/12 đến hết 11/12. Mục 8 nêu cách xử lý cụ thể cho cả hai.

> **Cách đọc báo cáo.**
> - **Dữ kiện có link nguồn, không kèm ghi chú:** lấy từ văn bản chính thức hoặc báo chí, đã được đối chiếu trong ghi chép nghiên cứu.
> - **"(MoMo tự công bố)":** số liệu do MoMo đưa ra, chưa có kiểm chứng độc lập.
> - **"(qua tóm tắt tìm kiếm)":** nhóm nghiên cứu chỉ thấy đoạn trích, chưa đọc toàn văn.
> - **"(suy luận)":** nhận định của người viết.
> - **"(kiến thức kỹ thuật chung)":** hiểu biết về mô hình và công cụ, không lấy từ ghi chép nghiên cứu.
>
> Mọi số liệu tính đến 24/11/2026. Hôm nay là thứ Ba 24/11, còn khoảng 9,5 ngày đến hạn nộp.

## 1. Đề thi thưởng cho sản phẩm thật, nơi AI làm việc thay người

Đề bảng sinh viên chỉ có một chủ đề lớn: **"Imagine the Future Workspace (Human Centered. AI Powered)"**. Câu dẫn của đề là: "Hãy tưởng tượng AI sẽ thay đổi cách đội ngũ fintech làm việc, và qua đó thay đổi cách con người mua sắm, thanh toán, quản lý tài chính và tự bảo vệ mình trên không gian số, rồi biến ý tưởng đó thành sản phẩm dùng được ngay hôm nay" ([exam.json](https://techday.momo.vn/content/exam.json)). Câu này có hai vế nối với nhau bằng chữ "qua đó". Vế đầu nói về cách *đội ngũ fintech* làm việc, vế sau nói về lợi ích cho *người dân*. Phần lớn các đội có lẽ sẽ chỉ làm vế sau; bài nào nói được cả hai vế sẽ có lợi thế tự nhiên (suy luận).

Phạm vi người dùng "không giới hạn" ("cá nhân, người bán, doanh nghiệp, đội vận hành…"), nhưng đội phải nêu rõ đối tượng trong slide. Sản phẩm phải thuộc ít nhất một trong ba chủ đề:
- **Trợ lý AI:** "hiểu nhu cầu và hành động thay người dùng", gồm năm nhánh mua sắm, cá nhân, thanh toán, bán hàng, tài chính.
- **An ninh mạng:** "phát hiện, ngăn chặn và phản ứng với các mối đe dọa".
- **Chống lừa đảo:** giúp người dùng "nhận diện và được cảnh báo trước… trước khi mất tiền hoặc thông tin".

Cụm "hành động thay người dùng" cho thấy đề muốn AI làm việc, không chỉ trả lời. Hai cụm "phản ứng" và "trước khi mất tiền" là ranh giới cần để ý khi xếp một ý tưởng vào chủ đề (suy luận).

Yêu cầu sản phẩm khắt khe hơn một hackathon thông thường. Sản phẩm phải "cụ thể, sử dụng được trực tuyến, không chỉ là bản trình diễn hay bản mẫu thử". Giám khảo "tự dùng thử… không phụ thuộc vào máy local của đội". Và "**AI là thành phần cốt lõi** tạo ra giá trị của sản phẩm, không chỉ là tính năng phụ" ([exam.json](https://techday.momo.vn/content/exam.json)). Bài nộp gồm bốn phần:
- hướng dẫn sử dụng tối đa 1 trang A4, có link và tài khoản dùng thử;
- mã nguồn .zip, kèm README khai báo tài sản có sẵn, thư viện mã nguồn mở và công cụ AI đã dùng;
- slide tối đa 10 trang PDF, "không được sửa sau khi nộp" và dùng luôn cho chung kết;
- video tối đa 3 phút quay sản phẩm chạy thật.

Các mốc và điều khoản chính trong thể lệ ([Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)):
- Hạn nộp **23:59:59 ngày 03/12/2026**. Danh sách 5 đội vào chung kết công bố trong ngày 08/12. Chung kết thi trực tiếp ngày 11/12 tại TP.HCM.
- Đội phải giữ sản phẩm truy cập được đến hết ngày thi. Điều 31.4 cấm "cập nhật Sản phẩm đang chạy tại đường link đã nộp, sau hạn chót".
- Không giới hạn ngôn ngữ lập trình hay mô hình AI (Điều 12.1). Được dùng thư viện, dataset, mô hình có sẵn nếu có quyền sử dụng hợp pháp (12.2).
- Phải khai báo nguồn dữ liệu cá nhân hoặc dữ liệu doanh nghiệp (12.4). Cấm nộp sản phẩm đã làm từ trước cho chính bài toán (12.5). Phải khai báo công cụ AI đã dùng (28.4).

Điểm quan trọng nhất cho việc chọn ý tưởng: **đề không cung cấp dữ liệu, API, sandbox hay credit nào của MoMo** (Điều 11; exam.json không liệt kê tài nguyên nào). Đội thi gồm 2–3 sinh viên quốc tịch Việt Nam từ 18 đến 23 tuổi, không ai đang làm việc cho MoMo, kể cả thực tập. Giải thưởng là 50, 30 và 20 triệu đồng; thành viên ba đội đứng đầu được vào thẳng vòng Leadership Interview của MoMo Talent 2027 ([content.json](https://techday.momo.vn/content/content.json)).

Thể lệ có ba tiêu chí chấm ([Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)):
- **Sáng tạo:** "ý tưởng mới, có tính đột phá hoặc cách tiếp cận khác biệt so với các giải pháp hiện có".
- **Chất lượng & mức độ hoàn thiện:** "sản phẩm tại thời điểm nộp bài: vận hành ổn định, người dùng có thể trải nghiệm trực tiếp".
- **Tiềm năng tác động:** "khả năng mở rộng trên quy mô lớn và số lượng người dùng có thể hưởng lợi".

**Trọng số không được công bố.** Ở vòng sơ loại, mỗi bài được ít nhất 3 giám khảo chấm độc lập. Cả bảy giám khảo đều làm công nghệ ở MoMo: CTO Thái Trí Hùng, Head of AI & Data Hồng Trung Dũng, một Research Scientist, hai lãnh đạo AI Engineering, một Sr. Manager Software Engineering và Head of ITC Hà Nội ([content.json](https://techday.momo.vn/content/content.json)). Từ đó có ba hệ quả (suy luận):
- Phần AI sẽ bị soi kỹ về kiến trúc, độ ổn định và cách đánh giá.
- Một sản phẩm hẹp mà chạy mượt có lợi hơn một sản phẩm rộng mà lỗi.
- Bất cứ thứ gì trùng với cái MoMo đang chạy sẽ bị nhận ra ngay, vì chính những người này đã xây nó.

Tinh thần của ban tổ chức lặp lại ở khắp website: "Human centered ✦ AI powered". CEO Nguyễn Mạnh Tường viết: "Hiểu con người để đặt đúng bài toán". CTO Thái Trí Hùng viết: "Dẫn dắt AI, đừng để AI dẫn dắt mình". Điều 3 của thể lệ ghi mục đích cuộc thi là "cùng nhau xây dựng cách làm việc hiệu quả giữa con người và AI trong tương lai" ([content.json](https://techday.momo.vn/content/content.json); [Thể lệ](https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf)). Năm 2024, CTO còn nói người dùng "không quan tâm đến việc chúng tôi ứng dụng AI ở đâu", và AI nên "khiêm nhường đến mức vô hình" ([CafeBiz, 31/10/2024](https://cafebiz.vn/tai-dinh-vi-thanh-tro-thu-tai-chinh-voi-ai-cac-sep-momo-da-noi-gi-176241031171910802.chn)). Trang chủ gọi đây là cuộc thi giải "bài toán thật của người dùng MoMo", còn đề thi ghi phạm vi người dùng "không giới hạn". Đề là văn bản cụ thể hơn. Dù vậy, chọn bài toán bám sát hệ sinh thái MoMo vẫn an toàn hơn cho tiêu chí tác động (suy luận).

Trên cùng máy chủ còn có một đề khác, file exam-internal.json, dành cho "Bảng nội bộ dành cho nhân viên MoMo". **Đề này không áp dụng cho sinh viên**; ở đây chỉ dùng nó làm tín hiệu về những gì lãnh đạo MoMo đang bận tâm ([exam-internal.json](https://techday.momo.vn/content/exam-internal.json)):
- Đề nội bộ yêu cầu sản phẩm "thể hiện rõ phần việc agent đảm nhận và phần việc con người kiểm soát hoặc ra quyết định".
- Đề tài trợ "Merchant SME 2027" nêu bối cảnh: MoMo phục vụ "khoảng 500.000 merchant SME, phần lớn chưa quen dùng công nghệ", muốn mở rộng lên 1 triệu, và phải "giữ chân merchant trước sự cạnh tranh của các ngân hàng" mà chi phí phục vụ không tăng.
- Các nhóm vấn đề của đề tài trợ gồm "Sản phẩm cho merchant SME low tech: số hóa, quản lý doanh thu, tài chính, thuế" và "Merchant Trust: Tiền về chắc chắn, sự cố được xử lý trước khi merchant phải gọi lên".

Đội sinh viên có thể lấy cảm hứng từ các vấn đề này, nhưng không được trình bày chúng như yêu cầu chính thức của bảng sinh viên.

| Ràng buộc (nguồn) | Hệ quả cho việc chọn và làm ý tưởng (suy luận) |
|---|---|
| Sản phẩm thật, giám khảo tự thử trực tuyến | Phạm vi hẹp nhưng chạy mượt; mỗi giám khảo có sandbox riêng; không phụ thuộc phần cứng hay quyền hệ điều hành đặc biệt |
| AI là thành phần cốt lõi | AI phải làm phần việc mà quy tắc cứng không làm được; tránh app thường gắn thêm chatbot |
| Không có dữ liệu hay API của MoMo | Chọn bài toán mà dữ liệu công khai (văn bản luật, thủ đoạn lừa đảo đã công bố, giọng nói) cộng dữ liệu giả lập vẫn đủ để AI có giá trị thật; khai báo trong README |
| Không được sửa sau 03/12, phải chạy đến 11/12 | Hạ tầng trả phí, luôn bật; có nhà cung cấp LLM dự phòng; đặt trần chi phí; đóng băng sản phẩm sớm |
| Slide không sửa được và dùng luôn cho chung kết | Làm slide ở chất lượng chung kết ngay từ đầu |
| Giám khảo là lãnh đạo kỹ thuật và AI của MoMo | Phải có kiến trúc rõ, bộ đánh giá, số đo trung thực; không lặp lại thứ MoMo đã có |
| 2–3 sinh viên, khoảng 9,5 ngày | Một luồng giá trị chính, tối đa ba tính năng lõi |

Từ các ràng buộc trên, có ba hướng sản phẩm hợp đề nhất:
1. Trợ lý *hành động* bên trong một luồng tiền cụ thể, không phải chatbot đa năng.
2. Phòng thủ ở những khâu MoMo chưa phủ: trước khi người dùng mở màn hình chuyển tiền, sau khi tiền đã đi, và phía người bán.
3. Công cụ cho người bán và đội vận hành, nơi thể hiện được mô hình "agent làm, con người duyệt" đúng tinh thần "Future Workspace".

## 2. MoMo đã phủ kín khâu giao dịch; khoảng trống nằm ở hai đầu và phía người bán

### Mô hình kinh doanh và quy mô

MoMo là tổ chức trung gian thanh toán có giấy phép ví điện tử 16/GP-NHNN. Theo Khoản 5 Điều 25 Thông tư 40/2024, ví **không được cấp tín dụng hay trả lãi** cho người dùng. Vì vậy Ví Trả Sau và Vay Nhanh do đối tác như TPBank, MBV, VCBNeo cung cấp, MoMo chỉ là kênh phân phối và hưởng phí ([VietnamFinance, 24/08/2026](https://vietnamfinance.vn/thu-phi-nguoi-dung-bai-toan-kho-cua-vi-dien-tu-d149537.html)).

Theo DealStreetAsia dẫn hồ sơ nộp cơ quan quản lý, năm 2024 MoMo có doanh thu **hơn 3.300 tỷ đồng**, lãi ròng **347,5 tỷ đồng** và chi phí bán hàng **1.990 tỷ đồng** ([BSA/DealStreetAsia, 14/05/2025](https://www.bsa.org.vn/momo-co-lai-trong-ca-nam-2024-tai-khoi-dong-ke-hoach-ipo/)). Chi phí bán hàng như vậy bằng khoảng 60% doanh thu, nên AI nào giảm được chi phí phục vụ hoặc chi phí khuyến mãi sẽ chạm vào dòng chi lớn nhất của MoMo (suy luận).

MoMo nói có **hơn 30 triệu người dùng**. Một báo cáo chứng khoán cho năm 2024 ghi hơn 40 triệu tài khoản đăng ký nhưng chỉ khoảng **10 triệu người dùng hoạt động hằng tháng** ([VnBusiness, 13/01/2026](https://vnbusiness.vn/bat-ngo-voi-so-von-dieu-le-cua-ky-lan-cong-nghe-momo.html)). Phía người bán, có **hơn 500.000** merchant và hộ kinh doanh dùng MoMo QR ([Tuổi Trẻ, 30/12/2025](https://tuoitre.vn/momo-va-hanh-trinh-15-nam-cung-tieu-thuong-viet-trong-chuyen-doi-so-20251230111814396.htm)), và hơn 200.000 điểm bán dùng loa thông báo (MoMo tự công bố, [momo.vn](https://www.momo.vn/tin-tuc/khuyen-mai/loa-bao-momo-nhan-tien-dung-chuan-tai-khoan-ho-8565)).

Áp lực cạnh tranh có thật. Chuyển khoản liên ngân hàng và VietQR miễn phí đã biến thanh toán P2P và QR thành hàng hóa phổ thông ([VietnamFinance](https://vietnamfinance.vn/thu-phi-nguoi-dung-bai-toan-kho-cua-vi-dien-tu-d149537.html)). Khảo sát Decision Lab quý 4/2024 cho thấy tỷ lệ người dùng coi app ngân hàng là nền tảng chính tăng lên 26% ([DNSE, 13/05/2025](https://www.dnse.com.vn/senses/tin-tuc/tung-la-ong-vua-vi-dien-tu-momo-va-zalopay-dang-dan-hut-hoi-truoc-doi-thu-quen-thuoc-35049338)).

### Định hướng chiến lược

Từ 29/10/2024, MoMo định vị mình là "Trợ thủ tài chính với AI" và nói muốn làm "trợ thủ chuyển đổi số cho doanh nghiệp" ([CafeBiz](https://cafebiz.vn/tai-dinh-vi-thanh-tro-thu-tai-chinh-voi-ai-cac-sep-momo-da-noi-gi-176241031171910802.chn)). Tại NExT Forum tháng 10/2026, đồng sáng lập Nguyễn Bá Diệp nói ba điều đáng chú ý ([Báo Pháp Luật](https://doanhnhan.baophapluat.vn/thuan-hoa-ten-lua-ai-cach-momo-dung-nguyen-ly-tesla-va-quy-dinh-thau-cam-de-giu-chan-nguoi-dung.md); [e.VnExpress, 18/10/2026](https://e.vnexpress.net/news/business/momo-co-founder-calls-for-simpler-more-user-friendly-technology-5134123.html)):
- Tính năng nào không phục vụ nhiều người thì bị bỏ.
- Lãnh đạo cấp cao gọi điện trực tiếp cho người dùng 2 giờ mỗi tháng.
- AI đang làm quản lý quá tải thông tin: hàng trăm báo cáo mỗi giờ, so với 30–40 báo cáo mỗi ngày trước đây.

Một ý tưởng tạo thêm báo cáo cho con người đọc sẽ đi ngược định hướng này. Một ý tưởng để AI gánh việc và con người chỉ duyệt sẽ đi cùng chiều (suy luận).

### Danh mục AI hiện có của MoMo

Bảng dưới tóm tắt các sáng kiến AI công khai của MoMo. Gần như mọi số liệu hiệu quả đều do MoMo tự công bố; ghi chép không tìm thấy kiểm toán hay đánh giá độc lập nào.

| Sáng kiến AI của MoMo | Kết quả công bố | Hạn chế có bằng chứng | Hệ quả cho ý tưởng thi |
|---|---|---|---|
| Chấm điểm rủi ro giao dịch thời gian thực (hơn 1.000 tín hiệu, 100–300 ms) và Graph Network | Khoảng 29.000 giao dịch bất thường/ngày; hơn 10.000 người được cảnh báo/ngày; 99,5% người được cảnh báo dừng lại; khoảng 15.000 tỷ đồng/năm được bảo vệ (MoMo tự công bố, [VnExpress, 29/05/2026](https://vnexpress.net/momo-dung-ai-quet-29-000-giao-dich-bat-thuong-moi-ngay-5078052.html)) | Không công bố tỷ lệ cảnh báo nhầm; nền tảng chỉ thấy "phút thứ 89"; tiền rời hệ thống trong chưa đến 30 phút ([VTC, 13/05/2026](https://vtcnews.vn/dung-ai-chong-lai-lua-dao-bang-ai-ar1017693.html)) | Không làm lại chấm điểm rủi ro |
| Nhãn cảnh báo tài khoản nhận xanh/vàng/đỏ và "Phản ánh giao dịch rủi ro", thử nghiệm từ 10/07/2025 ([MoMo](https://www.momo.vn/tin-tuc/thong-bao/an-tam-giao-dich-voi-2-tinh-nang-an-toan-bao-mat-7646)) | Không có số liệu riêng | Chỉ được mô tả cho chuyển tiền ngân hàng | Không làm "kiểm tra người nhận" |
| eKYC, liveness, iProov Flashmark (từ 9/2025, [Vietnam News](https://vietnamnews.vn/economy/1724972/momo-partners-with-iproov-to-strengthen-biometric-security.html)) | Mở tài khoản ngân hàng trong 2–3 phút (MoMo tự công bố) | Người xác thực lỗi phải nhờ người thân hoặc ra cửa hàng | Không làm bộ phát hiện deepfake cho eKYC |
| Chấm điểm tín dụng AI / Điểm Tin Cậy | Tỷ lệ duyệt tăng gấp đôi, xử lý nhanh 10–30 lần (MoMo tự công bố, [Đại biểu Nhân dân, 13/11/2024](https://daibieunhandan.vn/ung-dung-ai-de-giup-nguoi-viet-lam-duoc-nhieu-hon-voi-tien-10351809.html)); hai lần R&D đầu thất bại, lần thứ ba thành công nhờ phân tích quan hệ mạng lưới ([CafeF, 20/10/2025](https://cafef.vn/giam-doc-khoa-hoc-du-lieu-momo-bat-mi-2-lan-vap-nga-va-triet-ly-phia-sau-mo-hinh-ai-giup-hang-trieu-nguoi-khong-cic-tiep-can-tin-dung-ngan-hang-188251020145531603.chn)) | Không công bố nợ xấu hay ngưỡng điểm | Đội không có dữ liệu để cạnh tranh |
| Moni (chuyển từ kịch bản rule-based sang LLM, [momo.careers](https://momo.careers/blog/momo-tech-pioneers-the-minds-behind-ai-advancement-doi-ngu-dung-sau-tro-ly-ao-moni-2152)) và Quản lý chi tiêu | "Bước đầu được người dùng đón nhận" (MoMo tự công bố) | MoMo thừa nhận phân loại từng giao dịch "tốn nhiều thời gian" ([MoMo, 03/10/2025](https://www.momo.vn/tin-tuc/thong-bao/ban-tin-gop-y-va-tinh-nang-moi-thang-9-2025-8004)); không có bằng chứng Moni tự thực hiện tác vụ | Trợ lý chi tiêu là sân đã có chủ |
| Chatbot chăm sóc khách hàng GenAI | Khiếu nại hằng tuần giảm 75%, mức hài lòng tăng 23% (MoMo tự công bố, 2024) | CTO: "AI cannot replace customer service staff" ([TheInvestor](https://theinvestor.vn/ai-cannot-replace-customer-service-staff-momo-exec-d13110.html)) | Chỉ khác biệt được nếu AI có quyền hành động |
| AI cho merchant: nhập hóa đơn trong 10 giây, đề xuất mức ưu đãi ([MoMo Doanh nghiệp](https://www.momo.vn/dtdn), qua tóm tắt tìm kiếm); iPOS.vn, Nhanh.vn | Không có số liệu | Mảng mỏng nhất trong những gì MoMo công bố | Khoảng trống tương đối |
| Chiến dịch "TinAI? – Kiểm trước tin sau" cùng Bộ Công an và VTV, có game phân biệt nội dung người hay AI tạo ([VnExpress, 05/08/2026](https://vnexpress.net/momo-canh-bao-nguy-co-lua-dao-truoc-khi-chuyen-tien-5105527.html)) | Không có số liệu | Nền tảng chia sẻ tín hiệu liên ngành còn đang xây | Tránh làm game giáo dục nhận diện AI |

### Những khoảng trống chính MoMo thừa nhận

Các khoảng trống có bằng chứng tốt nhất đến từ chính lời MoMo:
- Hơn **90%** thiệt hại do người dùng bị thao túng rồi tự chuyển tiền. **76%** người bị lừa sẵn sàng rời nền tảng. **70%** nạn nhân dưới 25 tuổi, **50%** là sinh viên dưới 22 tuổi ([VnExpress, 29/05/2026](https://vnexpress.net/momo-dung-ai-quet-29-000-giao-dich-bat-thuong-moi-ngay-5078052.html)).
- Tiền rời hệ thống trong chưa đến 30 phút, còn điều tra liên nền tảng mất nhiều ngày ([VTC](https://vtcnews.vn/dung-ai-chong-lai-lua-dao-bang-ai-ar1017693.html)).
- Khả năng lấy lại tiền sau khi bị lừa thấp. Năm 2021, MoMo không hủy được các giao dịch đã hoàn tất ở merchant ([VietNamNet, 2021](https://vietnamnet.vn/nguoi-dung-vi-dien-tu-momo-bi-lua-mat-tien-vi-chu-quan-778291.html)).

Hai chi tiết sau quyết định mức trùng lặp của các ý tưởng về thuế:
- Bộ giải pháp cho tiểu thương mà MoMo công bố tháng 7/2025 **đã có** khai thuế online, hóa đơn điện tử, chữ ký số, đồng bộ kế toán và chấm điểm tín dụng từ dữ liệu giao dịch ([MoMo, 11/07/2025](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/bo-giai-phap-tai-chinh-tu-momo-giup-tieu-thuong-7891)).
- Tháng 3/2026, MoMo nói **đang lên kế hoạch** cho tờ khai thuế điền sẵn thông tin hộ ([MoMo, 20/03/2026](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-cap-nhat-moi-nhat-ve-giai-phap-nhan-tien-8587)). Đến 11/2026, ghi chép chưa xác minh được tính năng này đã ra mắt hay chưa.

Ngoài ra, ghi chép có liệt kê chiến dịch "Không Một Mình 2026" của MoMo nhưng không mô tả nội dung. Cần kiểm tra chiến dịch này có đụng tới hỗ trợ nạn nhân hay không trước khi chọn ý tưởng 30 Phút Vàng.

## 3. Người dùng đau nhất ở giao dịch treo, người bán đau nhất ở luật thuế mới

### 3.1 Người dùng cá nhân: sự cố giao dịch, lừa đảo thao túng và phí khó hiểu

Ghi chép có một phân tích review riêng ([Google Play](https://play.google.com/store/apps/details?id=com.mservice.momotransfer); [App Store VN](https://apps.apple.com/vn/app/id918751511)):
- Mẫu gồm 2.000 review mới nhất trên Google Play VN (15/10–23/11/2026) và 500 review App Store VN (09–23/11/2026).
- Review 1–2★ được tính là tiêu cực: 668 review, gán chủ đề bằng từ khóa tiếng Việt.
- Mẫu chỉ bao 5–6 tuần và có một sự cố ngày 05/11/2026 làm phồng số review xấu.

Vì vậy các con số dưới đây là **tín hiệu định hướng**, không đại diện cho toàn bộ người dùng.

| Chủ đề trong review tiêu cực | Google Play (558 review) | iOS (110 review) |
|---|---|---|
| Giao dịch lỗi, "đang xử lý" nhưng đã trừ tiền, chưa hoàn | **20,3%** | **32,7%** |
| App lag, bảo trì, không vào được | 20,1% | 18,2% |
| Liên kết ngân hàng, nạp và rút tiền | 11,3% | 10,9% |
| Tự động trừ tiền, gia hạn thuê bao | 10,0% | 10,9% |
| Chăm sóc khách hàng chậm, chỉ có trả lời tự động | 9,0% | 14,5% |
| Ví Trả Sau, vay, lãi, đòi nợ | 7,3% | 10,0% |
| Nhắc tới AI hoặc trợ thủ (hầu hết là chê) | 5,7% | 3,6% |
| Lừa đảo, bảo mật (phần lớn là người dùng gọi chính MoMo là "lừa đảo") | 3,4% | 10,0% |

**Giao dịch treo là nỗi đau lớn nhất.** Người dùng viết: "Chuyển tiền cho tiệm cơm bị lỗi 'đang chờ xử lý'… tiền vẫn bị trừ mà tiệm chưa nhận được tiền nên mình đã dùng tài khoản khác để chuyển", và "không lẽ cái hóa đơn vài chục mà đi tra soát". Chính sách của MoMo là không cho hủy giao dịch đang xử lý ([MoMo FAQ](https://www.momo.vn/hoi-dap/toi-co-the-huy-giao-dich-dang-cho-xu-ly-hoac-thuc-hien-lai-giao-dich-duoc-khong)); tiền bị trừ ở ngân hàng mà ví chưa cộng sẽ được hoàn trong 48 giờ ([MoMo FAQ](https://www.momo.vn/hoi-dap/nap-tien-tu-ngan-hang-tai-khoan-ngan-hang-bi-tru-tien-nhung-tai-khoan-momo-khong-thay-doi)). Hotline tính phí 1.000đ/phút ([MoMo, 20/08/2025](https://www.momo.vn/tin-tuc/thong-bao/khong-ranh-cong-nghe-van-co-the-chuyen-khoan-de-7826)). Gốc rễ là trạng thái giao dịch bất định giữa MoMo, ngân hàng và NAPAS, cộng với việc không có đường hủy hay hoàn tự động. Người dùng vì vậy trả lần hai qua kênh khác và mất tiền thật ở những khoản nhỏ không đáng tra soát (suy luận).

**Lừa đảo là nỗi đau được đo đạc tốt nhất ở tầm quốc gia.**
- Bộ Công an ghi nhận khoảng **4.200 vụ**, thiệt hại **khoảng 8.000 tỷ đồng** năm 2025 ([VOV](https://vov.vn/phap-luat/thiet-hai-tu-lua-dao-truc-tuyen-len-toi-8000-ty-dong-trong-nam-2025-post1286479.vov)).
- Khảo sát của Hiệp hội An ninh mạng Quốc gia (NCA) năm 2025: tỷ lệ nạn nhân giảm còn 0,18%; mạo danh công an là thủ đoạn số một; 34,13% người dùng gặp sự cố mã độc ([Dân trí, 08/01/2026](https://dantri.com.vn/cong-nghe/nam-2025-nan-lua-dao-truc-tuyen-giam-nguoi-viet-van-mat-hon-6000-ty-dong-20260107104833121.htm)).
- Hệ thống SIMO của Ngân hàng Nhà nước trong 9 tháng 2026: hơn 5,6 triệu lượt cảnh báo, hơn 1,9 triệu lượt dừng hoặc hủy giao dịch, hơn 6.300 tỷ đồng ([Vietstock, 08/10/2026](https://vietstock.vn/2026/10/hang-trieu-chu-tai-khoan-nhan-mot-canh-bao-hon-6300-ty-phai-tam-dung-757-1500164.htm)).
- Theo đưa tin về SIMO, cảnh báo vẫn dựa trên danh sách đen, và nạn nhân bị thao túng vẫn chuyển tiền dù đã qua OTP và sinh trắc ([Vietnam+, 15/07/2026](https://www.vietnamplus.vn/tu-nhung-cu-chuyen-khoan-vo-thuc-den-la-chan-canh-bao-som-post1124247.vnp)).

Lớp chống lừa đảo hiện tại cũng gây ma sát cho người dùng hợp lệ. Có ít review nhắc tới, nhưng rất cụ thể: "con AI chống lừa đảo tệ, bắt tôi phải đánh từng chữ"; "đang cần gấp mà cứ bắt 10 phút". Con số "99,5% dừng lại" của MoMo đo sự tạm dừng, không đo số vụ lừa bị ngăn (suy luận). Theo tính toán của nhóm nghiên cứu từ số liệu SIMO, chỉ khoảng một phần ba cảnh báo dẫn đến dừng hoặc hủy, tức phần lớn cảnh báo vẫn bị bỏ qua.

**Phí và các khoản trừ tự động gây cảm giác bị "gài".** Ví Trả Sau thu phí 33.000đ/tháng kể từ tháng có giao dịch thứ 6 ([MoMo – Biểu phí](https://www.momo.vn/vi-tra-sau/bieu-phi)). Review phàn nàn Ví Trả Sau bị chọn làm nguồn tiền mặc định. Năm 2024 có khách "bỗng dưng nợ" 1.194.000đ vì Ví Trả Sau trả tiền App Store ([CafeF, 01/04/2024](https://cafef.vn/vu-khach-hang-bong-dung-no-gan-12-trieu-dong-do-vi-tra-sau-momo-chinh-thuc-len-tieng-188240401151950347.chn)). Tuy vậy, tháng 9/2025 MoMo đã thêm tính năng đánh dấu giao dịch định kỳ, nhắc trước hạn và quản lý dịch vụ liên kết ([MoMo, 03/10/2025](https://www.momo.vn/tin-tuc/thong-bao/ban-tin-gop-y-va-tinh-nang-moi-thang-9-2025-8004)).

Về nền tảng tài chính cá nhân, chỉ khoảng **33%** người trưởng thành có tiền gửi tiết kiệm và **71%** có lịch sử tín dụng ([VnExpress, 24/02/2026](https://vnexpress.net/mot-phan-ba-nguoi-viet-truong-thanh-co-tien-tiet-kiem-tai-ngan-hang-5043736.html)). Công nhân bị đòi nợ gây sức ép, và thẩm định tín dụng "không phản ánh dòng tiền thực" ([CafeF, 19/11/2026](https://cafef.vn/tin-dung-den-cong-nhan-thuong-xuyen-bi-doi-no-gay-suc-ep-188261119161622784.chn)). Ngược lại, nhu cầu chia hóa đơn hay quỹ nhóm gần như không có bằng chứng: chỉ 2 trong 2.500 review nhắc tới. Không nên dựng ý tưởng chính trên đó.

### 3.2 Người bán: luật thuế mới, dữ liệu phân mảnh và lừa đảo tại quầy

**Quy mô và sức khỏe.** Việt Nam có khoảng **6,1 triệu hộ kinh doanh** với khoảng 10 triệu lao động. **81,5%** hộ giảm doanh thu năm 2025, và 55,2% coi kinh doanh là nguồn thu nhập *duy nhất* của gia đình ([VCCI, 19/05/2026](https://www.vcci.com.vn/tin-tuc/suc-khoe-ho-kinh-doanh-suy-giam-phan-lon-chi-lai-mong-hoac-hoa-von)). Theo Bộ Tài chính, khoảng 80% hộ có doanh thu từ 1 tỷ đồng/năm trở xuống nên không phải nộp thuế GTGT và TNCN; khoảng 20% còn lại có nghĩa vụ thuế ([Vietstock/VietNamNet, 28/07/2026](https://vietstock.vn/2026/07/ho-kinh-doanh-lo-kho-ke-khai-thue-bo-tai-chinh-noi-gi-758-1472527.htm)).

**Khung pháp lý đổi hẳn trong 2025–2026:**
- Bỏ thuế khoán từ 01/01/2026.
- Nghị định 68/2026 (ngày 05/03/2026): hộ tự khai, tự tính, tự nộp; phải thông báo **mọi tài khoản ngân hàng và ví điện tử** dùng cho kinh doanh ([Báo Chính phủ, 07/03/2026](https://baochinhphu.vn/tu-2026-ho-kinh-doanh-phai-bao-co-quan-thue-cac-tai-khoan-nhan-tien-102260307185152112.htm)).
- Hộ dưới ngưỡng thông báo doanh thu năm bằng mẫu 01/TKN-CNKD, hạn **31/01 năm sau**. Hộ trên ngưỡng khai theo quý. Doanh thu tính ngưỡng **gồm cả phần sàn thương mại điện tử đã khấu trừ** ([Thời báo Tài chính, 10/03/2026](https://thoibaotaichinhvietnam.vn/nghi-dinh-682026nd-cp-buoc-chuyen-quan-trong-trong-quan-ly-thue-ho-kinh-doanh-193417.html)).
- Nghị định 141/2026 nâng ngưỡng từ 500 triệu lên **1 tỷ đồng**, áp dụng cho kỳ tính thuế 2026. Hộ trên ngưỡng phải dùng hóa đơn điện tử; khi doanh thu lũy kế vượt 1 tỷ, phải đăng ký hóa đơn điện tử trong **30 ngày** ([chinhphu.vn, 25/05/2026](https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-141-2026-nd-cp-nang-nguong-doanh-thu-khong-phai-chiu-thue-len-1-ty-dong-119260504154326455.htm)).
- Thông tư 152/2025 quy định sổ kế toán theo nhóm nghĩa vụ; theo tóm tắt, chủ hộ có thể giao người thân làm kế toán ([Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/28/final-152signed-17695739990221209521402.pdf)).

Ngưỡng đã đi qua chuỗi 100 triệu → 200 triệu → 500 triệu → 1 tỷ ([Vietstock](https://vietstock.vn/2026/07/ho-kinh-doanh-lo-kho-ke-khai-thue-bo-tai-chinh-noi-gi-758-1472527.htm)). Lần đổi từ 500 triệu lên 1 tỷ diễn ra chưa đầy hai tháng sau Nghị định 68, nếu tính theo ngày ký 29/04/2026 mà các nguồn thứ cấp ghi.

**Nỗi đau tuân thủ có số liệu mạnh nhất cả báo cáo.** Khảo sát VCCI trên hơn 1.000 hộ ở 34 tỉnh thành (2–4/2026) cho thấy ([Thương hiệu & Công luận, 10/05/2026](https://thuonghieucongluan.com.vn/de-ho-kinh-doanh-khong-con-co-minh-truoc-rao-can-phap-ly-a317628.html)):
- **73,3%** coi quy định pháp luật và thủ tục là trở ngại lớn nhất.
- Khoảng 40% thường lo lắng khi tuân thủ quy định mới.
- Chỉ **13,9%** hiểu rõ quy định áp dụng từ đầu 2026; hơn 33% chỉ "nghe nói".
- **71,2%** khó lấy thông tin khách để xuất hóa đơn điện tử; **67,6%** lúng túng khi hạch toán chi phí được trừ; **66,8%** không theo kịp thay đổi chính sách.

Đặt cạnh số liệu khai thuế, bức tranh rõ hơn. Nửa đầu 2026, **99,6%** hộ đã khai điện tử và 98,1% đúng hạn; ứng dụng thuế đang được nâng cấp thêm chatbot AI ([Vietstock](https://vietstock.vn/2026/07/ho-kinh-doanh-lo-kho-ke-khai-thue-bo-tai-chinh-noi-gi-758-1472527.htm)). Như vậy nút thắt không nằm ở thao tác nộp, mà ở **khâu hiểu và ra được con số đúng** (suy luận).

Nỗi sợ có hệ quả thật:
- Tháng 6/2025, nhiều quán treo biển không nhận chuyển khoản vì tin đồn "truy thu 1,5%" ([VnExpress, 04/06/2025](https://vnexpress.net/nhieu-ho-kinh-doanh-tu-choi-nhan-chuyen-khoan-4894137.html)).
- Đến 3/2026, cơ quan thuế coi việc chỉ nhận tiền mặt là "dấu hiệu rủi ro cao" ([Thời báo Tài chính, 04/03/2026](https://thoibaotaichinhvietnam.vn/mot-bo-phan-ho-kinh-doanh-van-ne-thanh-toan-chuyen-khoan-de-che-giau-doanh-thu-193074.html)).

Dữ liệu doanh thu phân mảnh vì QR chủ yếu là "QR chuyển tiền" P2P, không có thông tin đơn hàng ([VnEconomy, 24/11/2025](https://vneconomy.vn/tu-chuyen-khoan-ca-nhan-den-thanh-toan-thuong-mai-chuan-quoc-gia.htm)).

Các công cụ hiện có đều miễn phí nhưng vẫn bắt người bán nhập liệu:
- MISA, Sapo, KiotViet.
- HDBank, Techcombank, Vietcombank tặng phần mềm và hóa đơn điện tử ([Tuổi Trẻ, 04/06/2026](https://tuoitre.vn/ho-kinh-doanh-het-ghi-chep-thu-cong-chuyen-sang-quan-ly-dong-tien-tren-nen-tang-so-20260603224956376.htm)).
- Agribank miễn phí gói số hóa đến 31/12/2028 (qua tóm tắt tìm kiếm, [Tạp chí Kinh tế Tài chính](https://tapchikinhtetaichinh.vn/ngan-hang-dong-hanh-ho-tro-ho-kinh-doanh-chuan-hoa-tai-khoan-149778.html)).

Mỗi ngân hàng chỉ thấy tài khoản của mình, nên không ai tổng hợp được doanh thu đa nguồn để canh ngưỡng (suy luận).

**Lừa đảo nhắm vào người bán đã có án thật:**
- Một đối tượng làm giả 309 ảnh "chuyển khoản thành công", chiếm hơn 13 tỷ đồng tiền vải của một tiểu thương chợ Ninh Hiệp (qua tóm tắt tìm kiếm, [Tuổi Trẻ, 01/09/2026](https://tuoitre.vn/photoshop-309-anh-chuyen-khoan-gia-chiem-doat-hon-13-ti-dong-tien-vai-cua-tieu-thuong-100260901115401713.htm)).
- Kẻ gian phát lại thông báo cũ trên loa, hoặc giả nhân viên lắp loa để chiếm OTP và eKYC ([CafeF, 07/09/2026](https://cafef.vn/canh-giac-voi-chieu-lua-dao-cai-dat-loa-bao-bien-dong-so-du-188260907091439869.chn)).
- Dán đè mã QR lên mã của cửa hàng ([Tuổi Trẻ, 2023](https://tuoitre.vn/nhieu-cua-hang-bi-ke-gian-dan-de-ma-qr-ngan-hang-de-chiem-doat-tien-20230825115347256.htm)).

Ở chợ truyền thống, nhiều tiểu thương lớn tuổi chỉ dùng điện thoại để nghe gọi và sợ nhầm khi đông khách (qua tóm tắt tìm kiếm, [Công Thương](https://congthuong.vn/so-hoa-cho-truyen-thong-huong-toi-phat-trien-ben-vung-450808.html)). Vì vậy giọng nói và loa, thứ họ đã quen, là giao diện hợp lý hơn bàn phím (suy luận).

## 4. Thị trường cho thấy AI thắng khi gắn vào hành động, niềm tin và chi phí tuân thủ

**Siêu ứng dụng châu Á.** Ant nói AI Pay vượt 100 triệu người dùng vào tháng 2/2026 ([PYMNTS](https://www.pymnts.com/?p=3503024)). Nhưng trợ lý chat đa năng Zhixiaobao được cho là "không đạt kỳ vọng" ([36Kr EU](https://eu.36kr.com/de/p/3857178983929091)). Với Ah Bao, một số người dùng sớm chỉ mở ra để chat thử thay vì làm tác vụ, và bài viết nhận định niềm tin giao tiền cho AI phụ thuộc vào cảm giác kiểm soát nhiều hơn năng lực kỹ thuật ([KrASIA, 22/07/2026](https://kr-asia.com/alipay-wants-more-than-a-supporting-role-in-the-ai-era)). Bài học: đo trợ lý bằng số tác vụ hoàn thành, không bằng số cuộc chat (suy luận).

**AI cho người bán có sức hút thật khi gắn vào thiết bị và dòng tiền.**
- Paytm AI Soundbox nói 11 ngôn ngữ Ấn Độ và tóm tắt doanh thu ([Business Today](https://www.businesstoday.in/tech-today/launch/story/paytm-unveils-indias-first-ai-soundbox-for-merchants-shares-jump-25-after-launch-497139-2025-10-07)); Paytm thu phí thuê bao và phí suy luận ([YourStory](https://yourstory.com/2025/11/paytms-q2-ai-soundbox-cautious-postpaid-revival-bnpl-lending)).
- Đến 12/2025, cứ 4 merchant đang hoạt động của Grab thì có 1 dùng trợ lý MAI ([Grab](https://www.grab.com/inside-grab/stories/new-tools-we-launched-in-2025-for-grab-merchants-to-boost-efficiency/)).
- Ngược lại, app sổ sách đứng riêng thu hẹp: Khatabook cắt nhân sự ([Inc42](https://inc42.com/buzz/khatabook-fires-over-40-employees-restructuring-exercise/amp)), OkCredit vẫn lỗ ([Inc42](https://inc42.com/buzz/tiger-global-backed-okcredit-narrows-fy25-loss-by-34-to-inr-23-cr/)). BukuWarung tăng trưởng nhờ chuyển sang thanh toán và cho vay ([Bisnis.com](https://teknologi.bisnis.com/read/20260127/84/1947604/bukuwarung-cetak-60-juta-transaksi-pada-2025-punya-8-juta-pengguna)).

Bài học trực tiếp cho Sổ Sẵn: sổ sách phải là sản phẩm phụ của dòng tiền QR, không đứng một mình.

**Chống lừa đảo hiệu quả nhờ thiết kế can thiệp, không chỉ nhờ mô hình chính xác hơn.**
- Ở Anh, đánh giá của PSR cho thấy tổn thất do lừa đảo chuyển tiền có ủy quyền (APP) qua Faster Payments giảm khoảng 21% sau khi bắt buộc hoàn tiền ([Regulation Tomorrow](https://www.regulationtomorrow.com/2026/07/payment-fraud-falls-by-73m-following-psr-reimbursement-scheme/)). UK Finance lại báo tổng tổn thất APP năm 2025 tăng 19%, lên £576,4 triệu ([UK Finance](https://www.ukfinance.org.uk/news-and-insight/press-release/fraud-report-2026-press-release)). Hai nguồn này mâu thuẫn, có thể do đo khác phạm vi.
- Úc dùng tính năng xác nhận người nhận hơn 100 triệu lần ([ABA](https://www.ausbanking.org.au/banks-hit-major-milestones-as-scam-fighting-technology-stops-thousands-of-risky-transfers/)).
- Singapore giảm khoảng 18% tổn thất năm 2025; tính năng Money Lock bảo vệ khoảng S$44 tỷ ([MHA](https://www.mha.gov.sg/media-room/newsroom/the-singapore-special-event-beyond-borders-a-whole-of-society-approach-to-disrupting-scams-internationally-at-the-2nd-global-fraud-summit/)).
- Revolut nói tổn thất lừa đảo thẻ liên quan merchant "đầu tư" giảm 30% nhờ luồng can thiệp ([Revolut](https://www.revolut.com/news/revolut_launches_ai_feature_to_protect_customers_from_card_scams_and_break_the_scammers_spell/)).
- Google Pay thí điểm cảnh báo khi người dùng đang gọi với số lạ và chia sẻ màn hình ([TechCrunch, 20/11/2025](https://techcrunch.com/2025/11/20/google-steps-up-ai-scam-protection-in-india-but-gaps-remain)).

**Tín dụng dựa trên dữ liệu ví có thực chất, nhưng rủi ro đẩy vay quá đà.**
- Khoảng 85–86% người vay của GCash lần đầu tiếp cận tín dụng chính thức ([Philstar](https://www.philstar.com/business/2026/08/09/2547919/building-trust-one-loan-time)).
- IFC kết luận dữ liệu thay thế *bổ sung chứ không thay thế* phương pháp truyền thống ([IFC, 5/2026](https://www.ifc.org/content/dam/ifc/doc/2026/cracking-the-credit-code-alternative-data-and-ai-for-financial-inclusion-summary.pdf)).
- Ở Kenya, tín dụng số dẫn tới nợ chồng nợ ([GSMA](https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/uncategorized/does-digital-credit-lead-to-over-indebtedness-evidence-from-a-study/)).
- Cleo AI phải trả 17 triệu USD để dàn xếp với FTC vì thiết kế lừa dối ([FTC](https://www.ftc.gov/news-events/news/press-releases/2025/03/cash-advance-company-cleo-ai-agrees-pay-17-million-result-ftc-lawsuit-charging-it-deceives-consumers)).

**Nhiều xu hướng còn là hype.**
- OpenAI gỡ tính năng thanh toán trong ChatGPT ngày 04/03/2026 ([Forrester](https://www.forrester.com/blogs/what-it-means-that-the-leader-in-agentic-commerce-just-pulled-back/)).
- Klarna phải tuyển lại người làm chăm sóc khách hàng ([Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)). CBA rút quyết định thay tổng đài viên bằng voice bot ([Bloomberg](https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots)).
- CFPB cảnh báo vòng lặp chatbot không thoát ra được người thật, gây hại nặng nhất cho người cao tuổi ([CFPB](https://consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance)).
- Báo cáo CCAF 2026: 81% tổ chức áp dụng AI nhưng chỉ 14% coi AI là yếu tố chuyển đổi chiến lược, và 55% thấy khó đo giá trị ([CCAF](https://www.jbs.cam.ac.uk/wp-content/uploads/2026/04/ccaf-2026-04-28-global-ai-in-financial-services-report.pdf)).

**Bức tranh Việt Nam.**
- Hơn 70% tổ chức tín dụng dùng AI/ML nhưng ít bên công bố hiệu quả tài chính ([VIR](https://vir.com.vn/banks-accelerate-ai-adoption-154052.html)).
- VCB Digibot xử lý 88,5% yêu cầu ([VNBA](https://vnba.org.vn/vi/tri-tue-nhan-tao--ai--day-nhanh-chuyen-doi-so-nganh-ngan-hang-15271.htm)). TPBank có VoicePay và ChatPay ([VnEconomy](https://vneconomy.vn/tpbank-ngan-hang-so-voi-ai-va-tu-dong-hoa.htm)).
- Zalo có chatbot "Chống lừa đảo" từ 12/2025 ([Nhân Dân](https://nhandan.vn/video-chatbot-ai-chong-lua-dao-tro-ly-an-ninh-mang-cua-ban-post938903.html)).
- Viettel đã huấn luyện mô hình tiếng Việt 120 tỷ tham số ([Thị trường Tài chính Tiền tệ](https://thitruongtaichinhtiente.vn/viettel-huan-luyen-thanh-cong-mo-hinh-ai-chu-quyen-tieng-viet-120-ty-tham-so-dat-hieu-suat-thuoc-nhom-dan-dau-cung-quy-mo-83392.html)). CMC công bố mô hình pháp luật 32B và bộ đánh giá VLegal-Bench ([VTC](https://vtcnews.vn/doanh-nghiep-ai-viet-nam-tren-ban-do-cong-nghe-the-gioi-ar1042792.html)).
- Ghi chép **không tìm thấy** ví điện tử nào ra mắt công cụ AI kê khai thuế cho hộ kinh doanh trong năm 2026.

**Khung pháp lý định hình thiết kế.**
- **Thông tư 53/2026/TT-NHNN** ký ngày 30/09/2026, hiệu lực từ 15/11/2026, áp dụng cả cho tổ chức trung gian thanh toán ([Thị trường Tài chính Tiền tệ](https://thitruongtaichinhtiente.vn/nhnn-ban-hanh-quy-dinh-ve-an-toan-quan-ly-rui-ro-khi-ung-dung-ai-trong-nganh-ngan-hang-86130.html)). Thông tư coi **AI tự động thanh toán vượt 10 triệu đồng/lần hoặc 20 triệu đồng/ngày** (với cá nhân) và **AI tự quyết tín dụng từ 50 triệu đồng** là rủi ro cao. Theo đưa tin, có thể từ bản dự thảo, chatbot phải báo ngay đầu phiên rằng người dùng đang tương tác với AI, và khách hàng phải có công cụ tạm dừng hoặc hủy quyền để AI tự thanh toán ([Vietnam+](https://www.vietnamplus.vn/ngan-hang-nha-nuoc-dat-nhieu-yeu-cau-khi-ngan-hang-ung-dung-ai-post1140808.vnp)).
- **Luật AI 134/2025** có hiệu lực từ 01/03/2026: chatbot phải cho người dùng biết họ đang tương tác với AI, và có thời gian chuyển tiếp 18 tháng cho ngành tài chính ([Allen & Gledhill](https://www.allenandgledhill.com/vn/publication/articles/32667/s-new-law-on-artificial-intelligence-risk-based-regulatory-framework-in-force-1-march-2026)).
- **Luật Bảo vệ dữ liệu cá nhân 91/2025:** dùng thông tin tín dụng để chấm điểm phải có sự đồng ý của chủ thể dữ liệu ([Bộ Công an](https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/bao-ve-du-lieu-ca-nhan-trong-mot-so-hoat-dong-1754989261)).
- **Nghị định 356/2025:** theo đưa tin, lịch sử giao dịch tài chính được xếp vào dữ liệu nhạy cảm ([PwC](https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html)).

| Bài học từ thị trường | Áp dụng cho ý tưởng thi (suy luận) |
|---|---|
| Trợ lý chat đa năng không tạo thói quen (Zhixiaobao, Ah Bao) | Trợ lý phải gắn vào một tác vụ có thời hạn và hậu quả thật |
| AI cho người bán sống được khi gắn vào thiết bị và dòng tiền (Paytm, Grab, BukuWarung) | Lấy dữ liệu QR và loa làm điểm tựa, không làm app sổ sách đứng riêng |
| Can thiệp đúng lúc hiệu quả hơn mô hình chính xác hơn (Anh, Úc, Singapore) | Ý tưởng chống lừa đảo nên sáng tạo ở *hành động*, không ở bộ phân loại |
| Thanh toán bằng agent ngoài Trung Quốc còn là trình diễn (OpenAI, Visa) | Không đặt cược vào "agent tự mua hàng" |
| Thay người bằng AI chỉ vì chi phí thì phải đảo chiều (Klarna, CBA, CFPB) | Luôn có đường thoát sang người thật; đo cả tỷ lệ giải quyết lẫn tỷ lệ liên hệ lại |
| Thông tư 53/2026 áp dụng cho trung gian thanh toán | Tuân thủ ngay từ thiết kế (báo đang dùng AI, có người duyệt, có nhật ký, có nút dừng) là điểm cộng |

## 5. Hai mươi mốt ý tưởng thô, sáu ý tưởng qua được bốn bộ lọc

Các ý tưởng dưới đây được sinh ra rộng có chủ đích: người dùng cá nhân, người bán, đội vận hành; trước, trong và sau giao dịch; cả các hướng ít hiển nhiên như lừa đảo nhắm vào người bán, phục hồi sau lừa đảo, giao dịch treo, thuế hộ kinh doanh. Mỗi ý tưởng phải qua bốn bộ lọc:
1. **Có bằng chứng nỗi đau độc lập**, không tự giả định MoMo gặp vấn đề.
2. **Không trùng** với thứ MoMo đã chạy.
3. **AI là lõi:** làm được việc mà quy tắc cứng không làm được.
4. **Làm thật được trong 9 ngày**, với dữ liệu công khai hoặc giả lập, để giám khảo tự thử trực tuyến.

| # | Ý tưởng | Chủ đề | Kết luận | Lý do then chốt |
|---|---|---|---|---|
| 1 | **Sổ Sẵn:** trợ lý thuế và sổ sách bằng giọng nói cho hộ kinh doanh, kèm bàn làm việc chính sách | Trợ lý AI + Chống lừa đảo | Phân tích sâu | Nỗi đau mạnh, có hạn chót, ít trùng, dữ liệu công khai đủ dùng |
| 2 | **30 Phút Vàng:** trợ lý phản ứng sau lừa đảo cho nạn nhân và chuyên viên | An ninh mạng + Chống lừa đảo | Phân tích sâu | Khoảng trống MoMo tự thừa nhận |
| 3 | **Tiền Về Thật:** xác minh tiền về cho người bán (ảnh chuyển khoản giả, đối soát) | Chống lừa đảo | Phân tích sâu | Có án thật; tín hiệu "Merchant Trust" |
| 4 | **Gỡ Rối Giao Dịch:** agent xử lý giao dịch treo và trả trùng | Trợ lý thanh toán | Phân tích sâu | Nỗi đau lớn nhất trong review |
| 5 | **Phòng Tập Chống Lừa:** nhận diện kịch bản và mô phỏng lừa đảo cho Gen Z | Chống lừa đảo | Phân tích sâu | Dữ liệu MoMo cho thấy nạn nhân trẻ |
| 6 | **Rõ Phí:** minh bạch chi phí và quyền trừ tiền tự động | Trợ lý thanh toán | Phân tích sâu (đối chứng) | Nỗi đau có thật nhưng MoMo đã xử lý một phần |
| 7 | AI hỏi mục đích trước khi chuyển tiền | Chống lừa đảo | Loại | MoMo đã có "điểm dừng có chủ đích" và câu hỏi xác nhận; cần tín hiệu rủi ro nội bộ; người dùng đã than ma sát |
| 8 | Phát hiện "đang gọi + chia sẻ màn hình" khi mở ví | Chống lừa đảo | Loại | Cần quyền hệ điều hành và app native, giám khảo khó tự thử; Google đã thí điểm |
| 9 | Người thân giám hộ tài chính cho người cao tuổi | Chống lừa đảo | Hạ xuống thành tính năng | 70% nạn nhân MoMo dưới 25 tuổi; bằng chứng về người già chỉ là các ca lẻ |
| 10 | Phát hiện tài khoản mule phía nhận | An ninh mạng | Loại | Cần đồ thị nội bộ; MoMo đã có Graph Network |
| 11 | Trợ lý giải thích Điểm Tin Cậy | Trợ lý tài chính | Loại | Không có mô hình thật để giải thích; MoMo không công bố ngưỡng |
| 12 | Tín dụng dòng tiền chống vay chồng cho tiểu thương | Trợ lý tài chính | Để vào lộ trình | Quyết định thuộc ngân hàng đối tác; Thông tư 53 coi khoản từ 50 triệu là rủi ro cao; cần sự đồng ý theo luật dữ liệu |
| 13 | Ví ủy quyền cho AI trả hóa đơn trong hạn mức | Trợ lý thanh toán | Loại khỏi nhóm đầu | Là hạ tầng, khác biệt thấp; thanh toán bằng agent đang thoái trào ngoài Trung Quốc |
| 14 | Trợ lý mua sắm so giá nhiều sàn | Trợ lý mua sắm | Loại | Phụ thuộc scraping và điều khoản sàn; không dùng tài sản của MoMo |
| 15 | Trợ lý cho chuyên viên xử lý 29.000 cờ gian lận mỗi ngày | An ninh mạng | Gộp vào #2 | Không biết công cụ nội bộ; ít người hưởng lợi trực tiếp |
| 16 | Loa thông báo biết trò chuyện cho tiểu thương lớn tuổi | Trợ lý bán hàng | Gộp vào #1 làm giao diện | Cần phần cứng; demo bằng web |
| 17 | AI soạn khuyến mãi nhắm khách quanh quán | Trợ lý bán hàng | Loại | Cần dữ liệu người dùng MoMo; MoMo đã có AI đề xuất mức ưu đãi |
| 18 | Số hóa hụi và quỹ nhóm có chấm điểm rủi ro | Trợ lý tài chính | Loại | Pháp lý mơ hồ; bằng chứng nhu cầu yếu |
| 19 | Thanh toán bằng giọng nói cho người ít chữ | Trợ lý thanh toán | Loại | TPBank VoicePay và Siri + MoMo đã có; giao dịch trên 10 triệu vẫn cần sinh trắc |
| 20 | "CFO AI" cho người bán nhiều sàn | Trợ lý tài chính | Gộp vào #1 | Nhập sao kê sàn, theo dõi thuế đã bị khấu trừ |
| 21 | Giải thích và kháng nghị khi bị chặn vì kiểm tra thiết bị | An ninh mạng | Loại | Hẹp; cần logic nội bộ |

## 6. Sáu ý tưởng dưới con mắt một giám khảo hoài nghi

### 6.1 Sổ Sẵn: trợ lý thuế và sổ sách bằng giọng nói cho hộ kinh doanh

| Hạng mục | Phân tích |
|---|---|
| Tên ý tưởng | **Sổ Sẵn:** "Hộ kinh doanh nói, AI ghi sổ và canh thuế", kèm bàn làm việc chính sách cho đội vận hành merchant |
| Đối tượng mục tiêu | Chính: chủ hộ nhỏ (tạp hóa, quán ăn, sạp chợ, người bán online) có nhận QR, nhất là nhóm quanh ngưỡng 1 tỷ và người lớn tuổi ít gõ phím. Phụ: con cháu làm kế toán theo Thông tư 152/2025; đội chăm sóc merchant và đội chính sách của ví |
| Pain point | Không biết mình phải khai gì, khi nào, đã vượt ngưỡng chưa; sợ sai bị phạt; sổ sách và chi phí phải nhập tay; doanh thu nằm rải ở nhiều tài khoản, ví và tiền mặt |
| Nguyên nhân và bản chất | (suy luận) Thiếu "lớp hiểu" chứ không thiếu công cụ nộp, vì 99,6% đã khai điện tử. Ba nguyên nhân gốc: (1) dữ liệu phân mảnh, vì QR chủ yếu là chuyển khoản P2P trong khi ngưỡng tính gộp mọi kênh; (2) luật đổi nhanh, ngưỡng 500 triệu thành 1 tỷ sau chưa đầy hai tháng; (3) văn bản viết cho người hiểu kế toán, còn người bán quen nói hơn quen gõ |
| Bằng chứng nỗi đau tồn tại | VCCI 2026: 13,9% hiểu rõ, 73,3% coi thủ tục là trở ngại lớn nhất, 71,2%, 67,6%, 66,8%, khoảng 40% lo lắng; 6,1 triệu hộ; 80% hộ dưới ngưỡng vẫn phải thông báo doanh thu năm; làn sóng né chuyển khoản 6/2025; khảo sát của MoMo trên 203 hộ cho thấy phần lớn còn quản lý thủ công ([MoMo, 11/07/2025](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/bo-giai-phap-tai-chinh-tu-momo-giup-tieu-thuong-7891)) |
| Giải pháp hiện có và hạn chế | Chatbot AI và eTax của ngành thuế, Sổ tay Cục Thuế: chung chung, không biết số liệu của từng hộ. MISA, Sapo, KiotViet, gói miễn phí của ngân hàng: phải nhập liệu, mỗi bên chỉ thấy tài khoản của mình. MoMo đã có khai thuế, hóa đơn điện tử, chữ ký số (7/2025) và kế hoạch tờ khai điền sẵn (3/2026): giải quyết khâu *nộp*, chưa giải quyết khâu *hiểu* |
| Giải pháp AI đề xuất | AI lo phần *hiểu* (giọng nói, ảnh hóa đơn, sao kê lộn xộn, văn bản luật); một máy luật tất định *tính* nghĩa vụ; con người *duyệt*. Bốn năng lực: (1) ghi sổ không cần gõ; (2) tách tiền bán hàng khỏi tiền gia đình và tiền chuyển giữa các tài khoản của chính mình; (3) canh ngưỡng 1 tỷ và dự báo ngày vượt; (4) hỏi đáp có trích điều khoản và nhận biết văn bản sửa đổi. Thêm bàn làm việc chính sách: AI đọc văn bản mới, đề xuất thay đổi quy tắc, nhân viên duyệt, hệ thống tính lại và báo cho đúng những hộ bị ảnh hưởng |
| Cách hoạt động và kịch bản sử dụng | (1) Cô Ba bán tạp hóa bấm mic: "Sáng nay bán hai thùng mì ba trăm nghìn tiền mặt, chú Tư nợ một trăm rưỡi". AI tạo hai bút toán và hỏi lại: "Chú Tư là khách ghi nợ quen, đúng không cô?". (2) Giao dịch QR và sao kê ngân hàng tự vào sổ; khoản "Me chuyen 2tr" được đánh dấu để cô xác nhận có phải tiền bán hàng không. (3) Màn hình Ngưỡng: lũy kế 812 triệu, dự báo vượt 1 tỷ cuối tháng 12 vì mùa Tết; nếu vượt, cô phải khai theo quý và đăng ký hóa đơn điện tử trong 30 ngày (trích Nghị định 141/2026). (4) Cô kể "có người xưng cán bộ thuế bảo chuyển phí hồ sơ"; AI cảnh báo mạo danh. (5) Cuối tháng 1, AI lập bản nháp số liệu thông báo doanh thu năm; con gái cô duyệt từ xa |
| Công nghệ, mô hình AI và dữ liệu | (kiến thức kỹ thuật chung) LLM đa phương thức qua API để trích xuất và soạn câu trả lời; mô hình nhỏ hơn để phân loại; nhận dạng giọng nói tiếng Việt; truy xuất lai BM25 + embedding đa ngôn ngữ trên kho luật chia theo Điều/Khoản, có ngày hiệu lực và quan hệ sửa đổi; máy luật viết bằng mã, mỗi quy tắc kèm trích dẫn; dự báo chuỗi thời gian có mùa vụ. Dữ liệu: văn bản luật công khai (Nghị định 68/2026, 141/2026, 70/2025; Thông tư 18/2026, 152/2025, 25/2025; Nghị quyết 198/2025), giao dịch giả lập, 100 ghi chú chuyển khoản do đội tự viết tay, 60 câu thoại tự thu |
| Điểm sáng tạo và khác biệt | (1) Nghĩa vụ được cá nhân hóa theo dòng tiền thật từ nhiều nguồn, điều mỗi ngân hàng không tự làm được. (2) Truy xuất nhận biết sửa đổi: RAG thông thường sẽ trả lời "500 triệu" vì Nghị định 68 ghi vậy. (3) Bàn làm việc chính sách thể hiện đúng hai vế của đề: AI đổi cách đội fintech làm việc, qua đó đổi cách người bán quản lý tài chính. (4) Giọng nói hướng tới loa mà MoMo đã phát cho khoảng 200.000 điểm bán |
| Giá trị cho người dùng và MoMo | Hộ kinh doanh: hiểu nghĩa vụ, không phải nhập tay, tránh bị phạt, tránh bị lừa bởi kẻ mạo danh cán bộ thuế. MoMo (suy luận): công cụ giữ chân merchant khi ngân hàng cho không phần mềm; bớt câu hỏi thuế dồn về chăm sóc khách hàng; có hồ sơ dòng tiền, khi chủ hộ đồng ý, để sau này mở tín dụng dòng tiền qua đối tác; thêm lý do để doanh thu tiếp tục chảy qua QR MoMo |
| Tính khả thi khi xây MVP | Cao. Dữ liệu cần thiết đều công khai hoặc giả lập hợp lệ; không cần API của MoMo; giám khảo thử được trên trình duyệt. Phần khó nhất là bộ đánh giá luật và hạ tầng ổn định, không phải mô hình |
| Khó khăn, rủi ro, hạn chế | AI trích sai luật khiến hộ bị phạt; luật tiếp tục đổi; trách nhiệm pháp lý; dữ liệu giao dịch là dữ liệu nhạy cảm; hộ có thể né QR vì sợ lộ doanh thu; ngân hàng miễn phí; nhận dạng giọng nói ở chợ ồn; chi phí suy luận so với doanh thu thấp từ mỗi hộ; MoMo có thể đang làm nội bộ |
| Phù hợp đề thi và khả năng cạnh tranh | Thuộc Trợ lý AI, nhánh tài chính và bán hàng: với 55,2% hộ, kinh doanh là nguồn thu duy nhất của gia đình, nên tài chính kinh doanh cũng là tài chính gia đình. Có thêm Chống lừa đảo qua cảnh báo mạo danh cán bộ thuế; 62,08% người dùng từng gặp mạo danh cơ quan chức năng, trong đó có thuế ([VnExpress International](https://e.vnexpress.net/news/tech/vietnamese-lose-744m-to-online-scams-in-2024-4828826.html)). Nói được cả hai vế của đề. Có lẽ khác biệt với số đông đội thi, vốn dễ chọn chatbot hoặc công cụ kiểm tra tin nhắn lừa đảo (suy luận) |

**Phản biện như một giám khảo MoMo, và cách khắc phục:**

| Câu hỏi hoài nghi | Điểm yếu thật | Cách khắc phục trong MVP |
|---|---|---|
| "Đây chỉ là RAG về thuế. Ngành thuế đã có chatbot AI." | Đúng, nếu sản phẩm chỉ có hỏi đáp | Hỏi đáp chỉ là một trong bốn năng lực; trọng tâm là nghĩa vụ cá nhân hóa từ sổ thật. Trình bày so sánh RAG thông thường với hệ thống nhận biết sửa đổi trên bộ câu hỏi chuẩn |
| "MoMo đã có khai thuế, hóa đơn điện tử và đang làm tờ khai điền sẵn." | Có trùng ở khâu nộp | Không làm khâu nộp. Xuất bản nháp số liệu sang công cụ hiện có. Định vị là lớp hiểu nằm trước khâu nộp và ghi rõ trên slide |
| "LLM bịa điều luật, hộ bị phạt thì ai chịu?" | Rủi ro nghiêm trọng nhất | LLM không bao giờ tự tính con số; mọi con số đến từ máy luật có trích dẫn. Kiểm tra câu trích có thật trong văn bản; tự từ chối khi không đủ căn cứ; có nút "hỏi kế toán viên"; ghi rõ hộ tự khai và tự chịu trách nhiệm theo Nghị định 68/2026 |
| "Ngân hàng cho không đến 2028, merchant dùng của bạn làm gì?" | Không thắng về giá | Thắng ở chỗ không phải nhập liệu, dùng giọng nói, gộp nhiều nguồn. Với MoMo đây là công cụ giữ chân, không phải nguồn thu |
| "Hộ sợ lộ doanh thu sẽ né QR." | Rủi ro hành vi có thật (6/2025) | Không tự gửi dữ liệu cho cơ quan thuế; dữ liệu thuộc chủ hộ; ghi cả tiền mặt; thông điệp "tuân thủ dễ, không bị phạt"; từ chối tư vấn né thuế |
| "Gửi dữ liệu giao dịch nhạy cảm ra LLM nước ngoài?" | Vấn đề thật khi triển khai thật | MVP chỉ dùng dữ liệu giả lập. Lộ trình: che thông tin cá nhân trước khi gọi mô hình, xin đồng ý riêng theo Nghị định 356/2025, cân nhắc LLM nội địa |
| "Chợ ồn, giọng miền thì sao?" | Chưa đo | Đo độ chính xác theo từng trường trên 60 câu thu ở môi trường ồn; luôn có thẻ xác nhận trước khi ghi; có ô nhập chữ dự phòng |
| "Dữ liệu đánh giá do chính bạn sinh ra thì vô nghĩa." | Nguy cơ tự kiểm tra chính mình | Tách bộ sinh dữ liệu khỏi bộ đánh giá; viết tay và gán nhãn tay 100 ghi chú chuyển khoản; công bố cả các lỗi |
| "Mỗi hộ tốn bao nhiêu tiền AI một tháng?" | Bài học Shopify về chi phí LLM ([MetaTrader/Zacks](https://www.metatrader.com/it/news/1706819-can-shopify-balance-sidekick-growth-with-higher-llm-costs)) | Dùng mô hình nhỏ để phân loại, cache câu hỏi phổ biến; đo lượng token mỗi hộ mỗi tháng và đưa lên slide |

### 6.2 30 Phút Vàng: trợ lý phản ứng sau lừa đảo

| Hạng mục | Phân tích |
|---|---|
| Đối tượng | Người vừa chuyển tiền cho kẻ lừa (theo dữ liệu MoMo, nhiều nhất là người trẻ và sinh viên); người thân hỗ trợ; chuyên viên chống gian lận và chăm sóc khách hàng của ví |
| Pain point | Phát hiện mình bị lừa thì hoảng loạn, không biết gọi ai trước, thiếu bằng chứng, dễ bị lừa tiếp bởi "dịch vụ lấy lại tiền" |
| Bản chất | (suy luận) Phần lớn thiệt hại là giao dịch do chính nạn nhân thực hiện nên không có "nút hủy". Cơ hội duy nhất là tốc độ và chất lượng thông tin trong một khoảng thời gian rất ngắn, qua nhiều bên: ngân hàng nhận, công an, ví |
| Bằng chứng | Hơn 90% thiệt hại do tự chuyển; 76% nạn nhân sẵn sàng rời nền tảng ([VnExpress, 29/05/2026](https://vnexpress.net/momo-dung-ai-quet-29-000-giao-dich-bat-thuong-moi-ngay-5078052.html)); tiền rời hệ thống trong chưa đến 30 phút ([VTC](https://vtcnews.vn/dung-ai-chong-lai-lua-dao-bang-ai-ar1017693.html)); khả năng lấy lại tiền thấp ([thutucphapluat.com](https://thutucphapluat.com/bai-viet/5652)); chỉ 45,69% nạn nhân báo cơ quan chức năng ([VnExpress International](https://e.vnexpress.net/news/tech/vietnamese-lose-744m-to-online-scams-in-2024-4828826.html)); có cảnh báo về "lừa đảo lần hai" (chỉ thấy tiêu đề, [CafeF, 31/08/2026](https://cafef.vn/canh-giac-voi-lua-dao-lan-hai-sau-khi-mat-tien-188260831155826124.chn)) |
| Hiện có và hạn chế | MoMo có "Báo cáo lừa đảo", "Phản ánh giao dịch rủi ro", hotline tính phí, khóa tài khoản qua chăm sóc khách hàng; ngân hàng có SIMO. Đây là các biểu mẫu, không dẫn dắt người dùng; chưa thấy lớp chống lừa lần hai nào được công bố. Cần kiểm tra trùng với chiến dịch "Không Một Mình 2026" |
| Giải pháp AI | Hội thoại hướng dẫn theo thời gian thực; trích xuất từ ảnh chụp tin nhắn và biên lai thành dòng thời gian; phân loại kịch bản theo các thủ đoạn đã được công an công bố; soạn sẵn đơn trình báo và đề nghị tra soát; lọc lừa đảo lần hai. Phía chuyên viên: hồ sơ có cấu trúc, gom cụm theo tài khoản nhận và kịch bản, đề xuất hành động để người duyệt |
| Kịch bản | Minh, sinh viên năm hai, chuyển 8 triệu "phí hồ sơ việc làm online". 40 phút sau thấy lạ, Minh mở 30 Phút Vàng và dán ảnh. AI dựng dòng thời gian, nhận ra kịch bản "việc nhẹ lương cao", đưa ra ba việc cần làm ngay kèm đồng hồ đếm ngược và đơn soạn sẵn. Hôm sau có tin nhắn "luật sư lấy lại tiền, phí 2 triệu"; AI cảnh báo đây là lừa đảo. Chuyên viên thấy hồ sơ của Minh nằm cùng cụm với 14 ca khác cùng tài khoản nhận, và bấm duyệt đề xuất phong tỏa (giả lập) |
| Công nghệ và dữ liệu | LLM đa phương thức, mẫu văn bản pháp lý, phân loại vài-mẫu (few-shot), gom cụm theo định danh trích xuất được. Dữ liệu là kịch bản giả lập dựa trên các thủ đoạn công an đã công bố |
| Sáng tạo | Cao: chuyển trọng tâm từ trước giao dịch (đã đông người làm) sang sau giao dịch (chưa ai làm bài bản). MoMo nói đang huấn luyện lại mô hình bằng phỏng vấn nạn nhân; ý tưởng này biến các cuộc phỏng vấn đó thành dữ liệu có cấu trúc |
| Giá trị | Nạn nhân hành động nhanh hơn, tránh mất tiền lần hai, bớt cô lập. MoMo (suy luận): giữ chân nhóm 76% muốn rời đi; giảm thời gian xử lý mỗi ca; có tín hiệu sớm về tài khoản nhận cho Graph Network. Để hình dung quy mô: nếu áp tỷ lệ 0,18% của NCA lên 30 triệu người dùng thì vào khoảng 54.000 người mỗi năm. Đây chỉ là phép nhân minh họa, không phải số liệu của MoMo |
| Khả thi | Phần mềm làm được, nhưng giá trị cốt lõi là phong tỏa tiền thật thì phải giả lập |
| Rủi ro | Không chứng minh được việc tăng tỷ lệ thu hồi tiền; lệch định nghĩa "Chống lừa đảo" (trước khi mất tiền); nội dung hỗ trợ tâm lý nhạy cảm; dữ liệu nạn nhân là dữ liệu nhạy cảm |
| Phù hợp và cạnh tranh | Hợp chủ đề An ninh mạng ("phản ứng", "truy vết") và Chống lừa đảo (ngăn lần mất tiền thứ hai). Rất gần mối quan tâm về niềm tin số của MoMo. Ít đội làm |

**Phản biện.** Câu hỏi khó nhất của giám khảo sẽ là: "Tiền đi trong 30 phút, nạn nhân thường phát hiện muộn hơn thế, vậy sản phẩm lấy lại được bao nhiêu?" Câu trả lời trung thực là không hứa thu hồi. Giá trị được bảo vệ được là bốn thứ: tốc độ cho những người phát hiện sớm, chặn lừa đảo lần hai, chất lượng bằng chứng, và tín hiệu có cấu trúc gửi về đội chống gian lận. Với lệch chủ đề, cách xử lý là khai chủ đề chính là An ninh mạng (phản ứng với mối đe dọa) và trình bày phần chặn lừa đảo lần hai như một cảnh báo *trước khi* mất tiền lần nữa. Về nội dung tâm lý, chỉ dùng kịch bản đã được rà soát, không để LLM tự do khuyên nhủ, và luôn kèm hotline thật.

### 6.3 Tiền Về Thật: xác minh tiền về cho người bán

| Hạng mục | Phân tích |
|---|---|
| Đối tượng và pain point | Người bán sỉ nhận đơn qua Zalo, quán đông khách, tạp hóa. Họ không chắc ảnh chuyển khoản khách gửi là thật, và không chắc thông báo trên loa là giao dịch mới |
| Bản chất | (suy luận) Ảnh thì dễ làm giả, loa chỉ phát âm thanh, chủ quán bận; tiền lại về nhiều tài khoản nên kiểm tra từng app mất thời gian |
| Bằng chứng | 309 ảnh giả, hơn 13 tỷ đồng ở Ninh Hiệp (qua tóm tắt tìm kiếm); chiêu phát lại thông báo loa và giả kỹ thuật viên lắp loa ([CafeF, 07/09/2026](https://cafef.vn/canh-giac-voi-chieu-lua-dao-cai-dat-loa-bao-bien-dong-so-du-188260907091439869.chn)); dán đè QR; theo một nghiên cứu của Visa, 43% doanh nghiệp nhỏ lo gian lận và chuyển nhầm (qua tóm tắt tìm kiếm, [VOV](https://english.vov.vn/en/economy/visa-highlights-vietnamese-payment-trends-for-2026-post1264446.vov)) |
| Hiện có và hạn chế | Công an khuyên kiểm tra số dư trên app ngân hàng trước khi giao hàng; MoMo QR 2.0 hiển thị rõ tài khoản cửa hàng ([MoMo](https://www.momo.vn/tin-tuc/thong-bao/moi-nang-cap-ma-qr-momo-the-he-20-buon-ban-an-tam-8413)). Cả hai đều phải làm thủ công, mỗi tài khoản một lần |
| Giải pháp AI | Đọc ảnh chuyển khoản của nhiều ngân hàng (đa phương thức) → trích xuất trường → đối chiếu với sổ (MoMo cộng sao kê đã nhập) → kết luận "Đã về / Chưa thấy / Nghi giả", kèm dấu hiệu bất thường về định dạng và thời gian |
| Sáng tạo và khác biệt | Khá cao; lừa đảo nhắm vào người bán đang bị bỏ ngỏ |
| Khả thi | Cao, nếu tái dùng sổ của Sổ Sẵn |
| Rủi ro | Phần đáng tin cậy nhất là đối chiếu sổ, vốn không cần nhiều AI; nhận diện ảnh giả là cuộc chạy đua không có hồi kết; chống phát lại trên loa cần mật mã ở thiết bị, không phải AI |
| Phù hợp | Chống lừa đảo; khớp tín hiệu "Tiền về chắc chắn" trong đề nội bộ (chỉ là tín hiệu). Nên làm thành mô-đun ưu tiên thấp của Sổ Sẵn, không đứng riêng |

### 6.4 Gỡ Rối Giao Dịch: agent xử lý giao dịch treo và trả trùng

| Hạng mục | Phân tích |
|---|---|
| Đối tượng và pain point | Mọi người dùng ví, nhất là khi trả tiền tại quán; người bán bị khách tưởng "ăn quỵt". Tiền đã bị trừ nhưng giao dịch "đang xử lý", người dùng trả lần hai, khoản nhỏ thì không đáng tra soát |
| Bản chất | Trạng thái bất định giữa MoMo, ngân hàng và NAPAS; không có đường hủy |
| Bằng chứng | Mạnh: 20,3% review tiêu cực trên Google Play và 32,7% trên iOS; FAQ "chờ 48 giờ"; MoMo từng chạy chương trình bồi thường 10.000đ cho giao dịch treo quá 2 giờ ([MoMo](https://www.momo.vn/tin-tuc/thong-bao/chuyen-tien-muot-hon-bao-gio-het-khong-can-doi-8878)) |
| Hiện có và hạn chế | Chatbot GenAI (MoMo tự công bố khiếu nại giảm 75%), ticket, hotline; review chê "trợ thủ AI… không giải quyết được gì" |
| Giải pháp AI | Agent có công cụ: đọc trạng thái giao dịch, phát hiện trả trùng cùng người nhận, tự mở yêu cầu hoàn tiền kèm bằng chứng, chủ động báo tiến độ, cho người bán xem "khách đã trả, tiền về lúc X". Nhân viên vận hành duyệt các khoản hoàn vượt ngưỡng |
| Sáng tạo | Trung bình: agent chăm sóc khách hàng là xu hướng chung (Toss, Klarna) |
| Khả thi | Trung bình: toàn bộ hệ thống nội bộ của MoMo phải giả lập, và giám khảo biết rõ cái gì là giả |
| Rủi ro | Gốc rễ nằm ở khâu đối soát backend, nên AI dễ bị xem là miếng băng dán; trùng với chatbot hiện có; dễ trông ngây thơ trước chính đội đã xây hệ thống |
| Phù hợp | Trợ lý thanh toán; tác động lớn nhưng khó thuyết phục về sáng tạo |

### 6.5 Phòng Tập Chống Lừa: nhận diện kịch bản và mô phỏng cho Gen Z

| Hạng mục | Phân tích |
|---|---|
| Đối tượng và pain point | Sinh viên và người trẻ bị thao túng qua kịch bản việc làm, đầu tư; một số bị dụ cho thuê tài khoản (Nghị định 340/2025 phạt 100–150 triệu đồng, [CafeF, 01/10/2026](https://cafef.vn/mua-ban-tai-khoan-ngan-hang-coi-chung-ruoc-hoa-vao-than-188261001071944878.chn)) |
| Bằng chứng | 70% nạn nhân dưới 25 tuổi, 50% là sinh viên dưới 22 tuổi (dữ liệu MoMo, [VnExpress](https://vnexpress.net/momo-dung-ai-quet-29-000-giao-dich-bat-thuong-moi-ngay-5078052.html)); NCA xếp hạng các thủ đoạn |
| Hiện có và hạn chế | Zalo có chatbot kiểm tra số điện thoại và link (12/2025); MoMo có chiến dịch "TinAI?". Thị trường đã đông |
| Giải pháp AI | (a) Radar: dán đoạn chat → AI xác định kịch bản và bước hiện tại ("bạn đang ở bước 'nộp phí kích hoạt'"); (b) mô phỏng: LLM đóng vai kẻ lừa, thích ứng theo người dùng, rồi phân tích lại sau buổi tập |
| Sáng tạo | Radar thấp; phần mô phỏng ở mức trung bình |
| Khả thi | Cao |
| Rủi ro | Khó chứng minh thay đổi hành vi; nhà cung cấp LLM có thể từ chối đóng vai kẻ lừa; nhiều đội khác có lẽ làm tương tự (suy luận) |
| Phù hợp | Đúng chủ đề Chống lừa đảo, nhưng khó nổi bật |

### 6.6 Rõ Phí: minh bạch chi phí và quyền trừ tiền tự động

| Hạng mục | Phân tích |
|---|---|
| Đối tượng và pain point | Người trẻ dùng Ví Trả Sau và các gói thuê bao; phí 33.000đ phát sinh mà không biết vì sao; nguồn tiền mặc định gây bất ngờ |
| Bằng chứng | Trừ tiền tự động khoảng 10% review tiêu cực; Ví Trả Sau 7–10%; vụ 1.194.000đ năm 2024 |
| Hiện có và hạn chế | MoMo đã thêm đánh dấu giao dịch định kỳ, nhắc trước hạn và quản lý dịch vụ liên kết (9/2025) |
| Giải pháp AI | Giải thích tổng chi phí trước khi trả ("đây là giao dịch thứ 6, sẽ phát sinh phí 33.000đ"), nhận diện thuê bao từ lịch sử giao dịch, bảng quản lý các quyền trừ tiền |
| Đánh giá | AI không phải lõi (phần lớn là quy tắc); có xung đột với doanh thu phí của MoMo; trùng một phần với tính năng đã có. Hợp làm góp ý tính năng cho Moni hơn là bài thi |

## 7. Sổ Sẵn dẫn bảng điểm vì cân bằng được tác động và khả thi

Thể lệ không công bố trọng số, nên bảng dưới cho các tiêu chí trọng số bằng nhau. Điểm từ 1 đến 5 là đánh giá của người viết (suy luận), dựa trên bằng chứng ở các mục trên. Các cột được ghép với tiêu chí chính thức như sau:
- "Sáng tạo" và "Ít trùng với MoMo" ứng với tiêu chí Sáng tạo.
- "Hoàn thiện được trong 9 ngày" ứng với Chất lượng & mức độ hoàn thiện.
- "Tác động và quy mô" và "Giá trị cho MoMo" ứng với Tiềm năng tác động.
- "AI là lõi" là điều kiện bắt buộc của đề.

| Ý tưởng | Sáng tạo | Hoàn thiện được trong 9 ngày | Tác động và quy mô | AI là lõi | Giá trị cho MoMo | Ít trùng với MoMo | Tổng /30 |
|---|---|---|---|---|---|---|---|
| **Sổ Sẵn** | 4 | 5 | 5 | 4 | 5 | 4 | **27** |
| 30 Phút Vàng | 5 | 4 | 3 | 4 | 4 | 4 | 24 |
| Tiền Về Thật | 4 | 4 | 3 | 3 | 4 | 5 | 23 |
| Gỡ Rối Giao Dịch | 3 | 3 | 5 | 3 | 4 | 2 | 20 |
| Phòng Tập Chống Lừa | 3 | 5 | 3 | 4 | 3 | 2 | 20 |
| Rõ Phí | 2 | 4 | 3 | 2 | 3 | 2 | 16 |

Thứ hạng khá vững khi đổi trọng số. Nhân đôi cột Sáng tạo: Sổ Sẵn 31, 30 Phút Vàng 29, Tiền Về Thật 27. Nhân đôi cột Tác động: Sổ Sẵn 32, 30 Phút Vàng 27, Tiền Về Thật 26, Gỡ Rối Giao Dịch 25. Nhóm đầu không đổi.

Các đánh đổi thể hiện rõ:
- Ý tưởng sáng tạo nhất (30 Phút Vàng) có tác động khó chứng minh nhất.
- Nỗi đau lớn nhất theo review (giao dịch treo) lại ít cần AI nhất và phụ thuộc nhiều nhất vào hệ thống nội bộ MoMo.
- Ý tưởng dễ làm nhất (Phòng Tập) nằm ở sân đông người nhất.

Sổ Sẵn không thắng ở chủ đề, vì công cụ thuế đã có nhiều. Nó thắng ở cách tiếp cận: cá nhân hóa theo sổ thật, nhận biết sửa đổi luật, và có bàn làm việc người–AI. Điểm yếu cảm tính là thuế kém "hấp dẫn" hơn chống lừa đảo trong mắt một hội đồng vừa nhận giải AI cho niềm tin số. Cách bù là kể câu chuyện bằng số liệu và bằng hai vế của đề thi.

**Quy tắc quyết định trước khi bắt tay làm.** Ngay hôm nay, hãy mở app Đối tác/Merchant MoMo và kiểm tra tờ khai điền sẵn hay trợ lý thuế đã ra mắt chưa. Nếu MoMo đã có một trợ lý thuế dùng AI theo đúng hướng này, chuyển sang 30 Phút Vàng. Nếu đội mạnh về bảo mật và an toàn LLM hơn là xử lý dữ liệu, 30 Phút Vàng cũng là lựa chọn hợp lý. Tiền Về Thật chỉ nên làm như một mô-đun của Sổ Sẵn.

## 8. Kế hoạch chín ngày đưa Sổ Sẵn lên sóng và giữ nó sống đến 11/12

### Phạm vi: làm thật gì, giả lập gì

| Mức ưu tiên | Hạng mục | Làm thật | Giả lập và khai báo |
|---|---|---|---|
| P0 | Sổ đa nguồn | Nhập giao dịch QR giả lập và file CSV sao kê; phân loại tiền bán hàng, tiền cá nhân, tiền hoàn, tiền chuyển giữa tài khoản của mình; loại trùng | Dữ liệu MoMo và ngân hàng đều giả lập, khai báo trong README theo Điều 12.4 |
| P0 | Ghi sổ bằng giọng nói và chữ | Nhận dạng giọng nói → trích xuất cấu trúc (món, số lượng, tiền, người nợ) → thẻ xác nhận | — |
| P0 | Canh ngưỡng và nghĩa vụ | Máy luật có phiên bản và ngày hiệu lực; dự báo ngày vượt 1 tỷ; liệt kê nghĩa vụ phát sinh | Chưa tính số thuế phải nộp cho đến khi đối chiếu được tỷ lệ % theo ngành trong văn bản gốc |
| P0 | Hỏi đáp có trích dẫn | Truy xuất nhận biết sửa đổi, kiểm tra trích dẫn, tự từ chối khi không đủ căn cứ | — |
| P0 | Bản nháp số liệu khai | Tổng hợp số liệu cho thông báo doanh thu năm và khai quý | Không nộp lên cổng thuế; không trình bày như mẫu chính thức |
| P0 | Sandbox cho từng giám khảo | Nút "Tạo cửa hàng mẫu mới" và "Đặt lại" | — |
| P1 | Bàn làm việc chính sách | AI đọc Nghị định 141 → đề xuất thay đổi quy tắc có trích dẫn → nhân viên duyệt → tính lại cho 1.000 hộ giả lập → soạn thông báo cho các hộ bị ảnh hưởng | Quần thể hộ là giả lập |
| P1 | Người thân duyệt từ xa | Link chỉ đọc, có ô bình luận | — |
| P1 | Cảnh báo mạo danh cán bộ thuế | Phân loại tin nhắn hoặc lời kể về cuộc gọi, kèm hướng dẫn | — |
| P1 | Ảnh hóa đơn đầu vào | Trích xuất thành dòng chi phí | — |
| P2 | Kiểm tra ảnh chuyển khoản (mô-đun Tiền Về Thật) | Đối chiếu với sổ | Ảnh mẫu do đội tự tạo |

Không làm: nộp tờ khai thật, chấm điểm tín dụng, dùng logo MoMo theo cách khiến người xem tưởng là sản phẩm chính thức. Giao diện ghi rõ "bản thử nghiệm độc lập cho hệ sinh thái MoMo".

### Kiến trúc và bộ đánh giá

Kiến trúc chia ba lớp: *AI hiểu, máy luật tính, con người duyệt*. Đây là cách trả lời trực tiếp câu "Dẫn dắt AI, đừng để AI dẫn dắt mình" của CTO.

| Lớp | Vai trò | Công nghệ (kiến thức kỹ thuật chung) |
|---|---|---|
| AI hiểu | Đọc giọng nói, ảnh, sao kê, văn bản luật | LLM gọi hàm (function calling) |
| Máy luật | Ngưỡng, nghĩa vụ, hạn nộp; mỗi quy tắc có trích dẫn và ngày hiệu lực | Quy tắc viết bằng mã |
| Lớp hội thoại | Lấy con số từ máy luật qua công cụ; không bao giờ để LLM tự tính | LLM kèm công cụ |
| Truy xuất | Kho luật chia theo Điều/Khoản, gắn quan hệ "được sửa đổi bởi" để Nghị định 141 ghi đè Nghị định 68 | BM25 + embedding đa ngôn ngữ |
| Vòng phản hồi | Khoản nào AI không chắc thì hỏi lại chủ hộ; câu trả lời thành nhãn mới | Học chủ động |

Các phương án công nghệ cụ thể (kiến thức kỹ thuật chung):
- Một LLM đa phương thức thương mại hỗ trợ tiếng Việt. Ghi chép cho thấy Grab dùng mô hình của OpenAI và Anthropic cho MAI ([Grab](https://www.grab.com/sg/press/others/grab-deploys-agentic-ai-to-empower-merchants-and-driver-partners/)), TPBank dùng nhiều LLM.
- Nhận dạng giọng nói tiếng Việt từ nhà cung cấp đám mây hoặc mô hình mã nguồn mở.
- Cơ sở dữ liệu quan hệ có hỗ trợ vector.
- Máy chủ luôn bật, không dùng gói miễn phí tự ngủ.

Bộ đánh giá là thứ phân biệt bài thi trước một hội đồng gồm Research Scientist và AI Engineering:
- **Hỏi đáp luật:** 120 câu hỏi chuẩn lấy từ Sổ tay Cục Thuế và các nghị định, chấm ba thứ: câu trả lời đúng, câu trích có thật và hỗ trợ được câu trả lời, tỷ lệ tự từ chối. Trong đó có khoảng 20 câu "bẫy sửa đổi" (văn bản gốc ghi 500 triệu, quy định hiện hành là 1 tỷ) để so với RAG thông thường.
- **Phân loại giao dịch:** độ chính xác trên 100 ghi chú chuyển khoản viết tay, gán nhãn tay, cộng 500 giao dịch giả lập.
- **Giọng nói:** độ chính xác theo từng trường trên 60 câu thu ở quán cà phê ồn.
- **Vận hành:** độ trễ p95 và chi phí token mỗi phiên.

Công bố số thật, kể cả khi chưa đẹp.

### Lịch làm việc mười ngày

| Ngày | AI và backend (A) | Giao diện và giọng nói (B) | Dữ liệu, luật, pitch (C) | Mốc kiểm tra |
|---|---|---|---|---|
| T3 24/11 | Chốt schema; khung máy luật | Khung web app chạy tốt trên điện thoại, đăng nhập, sandbox | Kiểm tra MoMo đã có trợ lý thuế chưa; đăng ký đội nếu chưa; gom văn bản luật | Chốt phạm vi |
| T4 25/11 | Bộ sinh dữ liệu giả lập; bộ phân loại v1 | Màn hình Sổ và màn hình Ngưỡng | Chia luật theo Điều/Khoản; bảng sửa đổi từ Nghị định 141 sang 68 | Sổ hiển thị từ dữ liệu giả |
| T5 26/11 | Truy xuất và kiểm tra trích dẫn | Thu âm và nhận dạng giọng nói | Viết 120 câu hỏi chuẩn | Hỏi đáp có trích dẫn chạy trọn luồng |
| T6 27/11 | Trích xuất bút toán từ giọng nói | Thẻ xác nhận, sửa lỗi | **Gửi email câu hỏi cho BTC trước 23:59**; thu 60 câu thoại | Nói một câu ra đúng bút toán |
| T7 28/11 | Dự báo ngưỡng; bản nháp số liệu khai | Bảng tổng quan | Đánh giá vòng 1 | Luồng demo chính chạy được |
| CN 29/11 | Bàn làm việc chính sách | Chia sẻ cho người thân; cảnh báo mạo danh | Đánh giá vòng 2, gom lỗi | Xong P1 hoặc cắt bỏ |
| T2 30/11 | Đưa lên production, LLM dự phòng, giới hạn tần suất, ghi log | Tối ưu cho điện thoại, HTTPS cho mic | Cho người ngoài dùng thử (chỉ dùng thử, không tham gia xây, theo Điều 31.2) | **Đóng băng tính năng lúc 23:59** |
| T3 01/12 | Sửa lỗi, kiểm tra tải | Quay video | Slide v1, hướng dẫn 1 trang | Có video thô |
| T4 02/12 | README: tài sản có sẵn, mã nguồn mở, công cụ AI (kể cả trợ lý viết code), nguồn dữ liệu; xóa khóa API khỏi mã nguồn | Dựng video hoàn chỉnh | Slide bản cuối | Chạy thử toàn bộ quy trình nộp |
| T5 03/12 | Nộp trước 18:00; kiểm tra link từ mạng và thiết bị khác | | | Đóng băng; từ đây chỉ giám sát |

Bốn câu hỏi nên gửi BTC trước 23:59 ngày 27/11. Câu trả lời sẽ thành "FAQ chính thức" theo Điều 13.
1. Sản phẩm độc lập, chạy ngoài app MoMo, có hợp lệ không?
2. Có được dùng tên và nhận diện MoMo trong giao diện thử nghiệm không?
3. Nếu máy chủ sập sau 03/12, khởi động lại mà không đổi mã có bị coi là "cập nhật sản phẩm" không?
4. Có credit đám mây từ nhà tài trợ không?

### Kịch bản video 3 phút

| Thời điểm | Hình ảnh | Thông điệp |
|---|---|---|
| 0:00–0:20 | Cô Ba ở quầy tạp hóa, giọng hỏi "Năm nay con có phải khai thuế không?" | 2026 bỏ thuế khoán; chỉ 13,9% hộ hiểu rõ quy định |
| 0:20–0:50 | Bấm mic, nói một câu bán hàng; thẻ xác nhận hiện ra; AI hỏi lại khoản nợ | Ghi sổ không cần gõ |
| 0:50–1:20 | Sổ tự gom QR và sao kê; khoản "Me chuyen 2tr" được hỏi lại | AI tách tiền gia đình khỏi doanh thu, con người quyết |
| 1:20–1:50 | Màn hình Ngưỡng: 812 triệu, dự báo vượt cuối tháng 12; nghĩa vụ phát sinh, trích Nghị định 141 | Cá nhân hóa theo dòng tiền thật |
| 1:50–2:15 | Hỏi về chi phí được trừ; dán tin nhắn "cán bộ thuế" đòi chuyển tiền | Trả lời có trích dẫn; cảnh báo mạo danh |
| 2:15–2:40 | Bàn làm việc chính sách: nạp Nghị định 141 → AI đề xuất thay đổi → nhân viên duyệt → 312 hộ được báo | AI đổi cách đội fintech làm việc, qua đó đổi cách người bán tuân thủ |
| 2:40–3:00 | Số đo của bộ đánh giá; 6,1 triệu hộ, 500.000 merchant | Tác động và đường đi vào hệ sinh thái MoMo |

### Cốt truyện slide 10 trang

| Trang | Nội dung |
|---|---|
| 1 | Tên, câu giá trị, đối tượng (hộ kinh doanh và đội vận hành merchant), chủ đề khai báo (Trợ lý AI và Chống lừa đảo) |
| 2 | Vấn đề: 6,1 triệu hộ, bỏ thuế khoán, 13,9%, 73,3%, mốc 31/01/2027 |
| 3 | Bản chất: dữ liệu phân mảnh, luật đổi nhanh, giao diện chữ |
| 4 | Giải pháp hiện có và khoảng trống: 99,6% đã khai điện tử nhưng khai được không có nghĩa là hiểu |
| 5 | Sổ Sẵn: ba hành động và một bàn làm việc |
| 6 | Bốn ảnh chụp luồng demo |
| 7 | Kiến trúc: AI hiểu, máy luật tính, con người duyệt; các lớp chặn sai sót |
| 8 | Đánh giá: số đo thật, có so sánh với RAG thông thường |
| 9 | Tác động và độ khớp với MoMo: giữ chân merchant, giảm chi phí phục vụ, đường tới tín dụng có sự đồng ý; tuân thủ |
| 10 | Rủi ro và cách khắc phục, lộ trình (loa, app Merchant), đội |

### Tài liệu nộp và tuân thủ ngay từ thiết kế

**Hướng dẫn một trang** cho giám khảo đi theo đúng bốn bước của video: chọn hoặc tạo cửa hàng mẫu, nói một câu bán hàng, xem màn hình Ngưỡng, hỏi một câu về thuế. Thêm bước năm: mở bàn làm việc chính sách bằng vai trò nhân viên.

Sản phẩm cần có sẵn các lớp tuân thủ sau:
- Báo ngay đầu phiên rằng người dùng đang trò chuyện với AI, theo Luật AI và tinh thần Thông tư 53.
- Màn hình xin đồng ý dùng dữ liệu giao dịch, và nút xóa dữ liệu.
- Nhật ký mọi câu trả lời kèm nguồn.
- Từ chối tư vấn né thuế.
- Không tự nộp hồ sơ thay người dùng.

Sổ Sẵn không thực hiện thanh toán và không quyết định tín dụng, nên có lẽ nằm ngoài các ngưỡng rủi ro cao của Thông tư 53 (suy luận, cần đối chiếu toàn văn).

### Rủi ro khi giám khảo tự thử và khi thuyết trình

| Rủi ro | Cách giảm |
|---|---|
| Nhà cung cấp LLM sập hoặc hết hạn mức trong 8 ngày không được sửa | Có nhà cung cấp dự phòng tự chuyển; nạp trước tiền; trần chi phí; cache câu trả lời cho các câu hỏi chuẩn |
| Ba giám khảo trở lên cùng dùng một tài khoản, dữ liệu đè lên nhau | Mỗi phiên một sandbox; nút đặt lại |
| Trình duyệt chặn mic hoặc phòng chung kết ồn | Bắt buộc HTTPS; bấm-để-nói; luôn có ô nhập chữ |
| Trích sai điều luật | Kiểm tra trích dẫn, tự từ chối, có nút người thật |
| Máy chủ ngủ hoặc chứng chỉ hết hạn | Máy chủ luôn bật; kiểm tra hạn tên miền và SSL đến sau 11/12 |
| Lộ khóa API trong file .zip | Dùng biến môi trường; quét bí mật trước khi nộp |
| Giám khảo hỏi câu ngoài phạm vi kho luật | Trả lời "chưa đủ căn cứ" và chỉ kênh chính thức |

### Phương án dự phòng: MVP của 30 Phút Vàng

Nếu chuyển hướng, giữ cùng nhịp mười ngày. MVP gồm:
- Phòng chat cho nạn nhân, nhận chữ và ảnh chụp.
- Trích xuất dòng thời gian và phân loại kịch bản theo thủ đoạn công an đã công bố.
- Danh sách việc cần làm có đồng hồ đếm ngược.
- Bản nháp đơn trình báo và đề nghị tra soát.
- Bộ lọc lừa đảo lần hai.
- Bảng điều khiển cho chuyên viên, có gom cụm theo tài khoản nhận và nút duyệt đề xuất.

Phong tỏa tài khoản, kết nối SIMO và phản hồi của ngân hàng đều giả lập và khai báo trong README. Video nên kể trọn câu chuyện của Minh trong 3 phút và kết bằng góc nhìn của chuyên viên duyệt cụm 15 ca.

## Kết luận

Bài học quan trọng nhất từ nghiên cứu này là tìm lợi thế ở đúng chỗ. AI của MoMo mạnh nhất ở nơi dữ liệu nằm *bên trong* MoMo: rủi ro giao dịch, tín dụng, cá nhân hóa. Đội sinh viên không có dữ liệu đó, nên chỉ thắng được ở nơi tri thức *công khai nhưng lộn xộn*: văn bản luật đổi liên tục, thủ đoạn lừa đảo đã công bố, lời nói của người bán ở chợ. Ở đó, dữ liệu giả lập cộng nguồn công khai vẫn đủ để AI làm việc thật. Cũng từ đó, câu đề "AI thay đổi cách đội ngũ fintech làm việc, và qua đó…" trở thành một tiêu chí ngầm. Đội nào cho giám khảo thấy một vòng người–AI cụ thể, AI đề xuất và con người duyệt, rồi tác động lan tới hàng triệu người dùng, sẽ khác biệt với phần đông chỉ làm vế sau của đề.

Điều quyết định trước một hội đồng toàn kỹ sư và nhà nghiên cứu AI không phải là mô hình mới nhất, mà là sự trung thực khi đánh giá. Một bài thi chỉ ra được lỗi "500 triệu hay 1 tỷ" mà RAG thông thường mắc phải, đo được lỗi của chính mình và để LLM tránh xa phần tính toán sẽ thuyết phục hơn một bản demo mượt mà không có số đo. Thời điểm cũng đang đứng về phía Sổ Sẵn: chung kết rơi đúng vào tháng cuối trước chu kỳ khai năm đầu tiên sau khi bỏ thuế khoán. Đó là thứ "dùng được ngay hôm nay" theo nghĩa đen của đề.
