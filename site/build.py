"""Build the shareable report page and the policy-sources appendix from the research report."""
import html
import re
import subprocess
import sys
from pathlib import Path

REPORT = Path(sys.argv[1])
TEMPLATE = Path(sys.argv[2])
OUT = Path(sys.argv[3])
APPENDIX_MARK = "## Phụ lục: Văn bản pháp lý và nguồn"

# status: ok = read a source page carrying the instrument's content; mid = via press/law-firm summaries;
# low = only via search snippets, or sources conflict.
LAWS = [
    ("Thuế và hộ kinh doanh", [
        dict(id="l-nq198", name="Nghị quyết 198/2025/QH15", sub="Quốc hội",
             dates=[("Ban hành", "17/05/2025"), ("Áp dụng phần được dùng", "01/01/2026")],
             points=["Điều 10 khoản 6: bỏ thuế khoán với hộ, cá nhân kinh doanh từ 01/01/2026.",
                     "Điều 10 khoản 7: chấm dứt lệ phí môn bài từ 01/01/2026."],
             status="low", status_text="Chỉ thấy qua đoạn trích tìm kiếm của hai trang tóm tắt; chưa đọc văn bản.",
             sources=[("LuatVietnam", "https://luatvietnam.vn/thue-phi-le-phi/10-chinh-sach-moi-ve-thue-phi-theo-nghi-quyet-198-2025-qh15-565-102213-article.html"),
                      ("Thư viện nhà đất", "https://thuviennhadat.vn/phap-luat/nghi-quyet-198-bo-thue-khoan-bo-le-phi-mon-bai-tu-01-01-2026-680780.html")]),
        dict(id="l-nd68", name="Nghị định 68/2026/NĐ-CP và Thông tư 18/2026/TT-BTC", sub="Chính sách thuế và quản lý thuế với hộ, cá nhân kinh doanh",
             dates=[("Ban hành", "05/03/2026"), ("Hiệu lực", "từ ngày ban hành")],
             points=["Hộ tự khai, tự tính, tự nộp thuế.",
                     "Phải thông báo mọi tài khoản ngân hàng và ví điện tử dùng cho kinh doanh (Khoản 4 Điều 13); hộ đang hoạt động nộp mẫu 01/BK-STK chậm nhất 20/4/2026.",
                     "Hộ dưới ngưỡng thông báo doanh thu thực tế mỗi năm một lần qua mẫu 01/TKN-CNKD, hạn 31/01 năm sau. Hộ trên ngưỡng khai theo quý (mẫu 01/CNKD).",
                     "Doanh thu tính ngưỡng gồm cả doanh thu đã được tổ chức khác khấu trừ hoặc nộp thay."],
             status="mid", status_text="Đã đọc bài của Báo Chính phủ và Thời báo Tài chính Việt Nam; chưa đọc nguyên văn nghị định.",
             sources=[("Báo Chính phủ · 07/03/2026", "https://baochinhphu.vn/tu-2026-ho-kinh-doanh-phai-bao-co-quan-thue-cac-tai-khoan-nhan-tien-102260307185152112.htm"),
                      ("Thời báo Tài chính VN · 10/03/2026", "https://thoibaotaichinhvietnam.vn/nghi-dinh-682026nd-cp-buoc-chuyen-quan-trong-trong-quan-ly-thue-ho-kinh-doanh-193417.html")]),
        dict(id="l-nd141", name="Nghị định 141/2026/NĐ-CP", sub="Sửa Nghị định 68/2026 và Nghị định 320/2025",
             dates=[("Ngày ký", "29/04/2026, chỉ có ở nguồn thứ cấp"), ("Đăng toàn văn", "25/05/2026 trên chinhphu.vn"), ("Áp dụng", "kỳ tính thuế 2026, từ 01/01/2026")],
             points=["Thay “500 triệu đồng” bằng “01 tỷ đồng” ở các Điều 3, 4, 8, 9, 10, 11, 12, 17, 18 của Nghị định 68/2026.",
                     "Doanh thu trên 1 tỷ đồng/năm phải dùng hóa đơn điện tử có mã hoặc khởi tạo từ máy tính tiền; từ 1 tỷ trở xuống được tự chọn.",
                     "Doanh thu lũy kế vượt 1 tỷ trong năm: đăng ký hóa đơn điện tử trong 30 ngày sau kỳ tính thuế vượt ngưỡng.",
                     "Bộ Tài chính (7/2026): khoảng 80% hộ có doanh thu từ 1 tỷ trở xuống nên không phải nộp GTGT, TNCN; 99,6% hộ khai thuế điện tử trong nửa đầu 2026."],
             status="ok", status_text="Nội dung đối chiếu trên trang toàn văn của chinhphu.vn. Ngày ký chưa xác nhận vì trang chính phủ không ghi.",
             sources=[("chinhphu.vn · 25/05/2026", "https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-141-2026-nd-cp-nang-nguong-doanh-thu-khong-phai-chiu-thue-len-1-ty-dong-119260504154326455.htm"),
                      ("VnEconomy", "https://vneconomy.vn/ho-kinh-doanh-co-doanh-thu-duoi-1-ty-dong-chua-bat-buoc-dung-hoa-don-dien-tu.htm"),
                      ("LuatVietnam", "https://luatvietnam.vn/tin-van-ban-moi/chinh-thuc-nang-nguong-doanh-thu-len-1-ty-dong-doi-voi-ho-kinh-doanh-tu-2026-186-108719-article.html"),
                      ("Bộ Tài chính qua Vietstock · 28/07/2026", "https://vietstock.vn/2026/07/ho-kinh-doanh-lo-kho-ke-khai-thue-bo-tai-chinh-noi-gi-758-1472527.htm")]),
        dict(id="l-nd70", name="Nghị định 70/2025/NĐ-CP", sub="Sửa Nghị định 123/2020 về hóa đơn, chứng từ",
             dates=[("Ban hành", "20/03/2025"), ("Hiệu lực", "01/06/2025")],
             points=["Hộ có doanh thu từ 1 tỷ đồng/năm trở lên trong một số ngành (ăn uống, khách sạn, bán lẻ, vận tải hành khách, làm đẹp, vui chơi…) phải dùng hóa đơn điện tử khởi tạo từ máy tính tiền kết nối cơ quan thuế."],
             status="mid", status_text="Qua bài tóm tắt của LuatVietnam và PwC Việt Nam; chưa đọc toàn văn.",
             sources=[("LuatVietnam", "https://luatvietnam.vn/tin-van-ban-moi/5-truong-hop-bat-buoc-su-dung-hoa-don-khoi-tao-tu-may-tinh-tien-tu-01-6-2025-186-101567-article.html"),
                      ("PwC Việt Nam · 16/04/2025", "https://www.pwc.com/vn/vn/publications/news-brief/250416-changes-to-invoicing-regulations.html")]),
        dict(id="l-tt152", name="Thông tư 152/2025/TT-BTC", sub="Chế độ kế toán hộ, cá nhân kinh doanh; thay Thông tư 88/2021",
             dates=[("Ban hành", "31/12/2025"), ("Hiệu lực", "01/01/2026")],
             points=["Chia nhóm sổ theo nghĩa vụ thuế thực tế, mỗi nhóm 1–4 sổ.",
                     "Chủ hộ tự ghi hoặc giao bố mẹ, vợ chồng, con, anh chị em ruột làm kế toán.",
                     "Lưu trữ sổ tối thiểu 5 năm."],
             status="mid", status_text="Có link toàn văn trên Công báo; nội dung trong ghi chép lấy cùng các bài tóm tắt.",
             sources=[("Công báo (PDF)", "https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/28/final-152signed-17695739990221209521402.pdf"),
                      ("Sapo", "https://www.sapo.vn/blog/thong-tu-152-2025-tt-btc"),
                      ("Thư viện pháp luật", "https://thuvienphapluat.vn/phap-luat-doanh-nghiep/cong-viec-phap-ly/che-do-ke-toan-ho-kinh-doanh-527.html")]),
        dict(id="l-nd117", name="Nghị định 117/2025/NĐ-CP", sub="Quản lý thuế với kinh doanh trên nền tảng thương mại điện tử, nền tảng số",
             dates=[("Ban hành", "09/06/2025"), ("Hiệu lực", "01/07/2025")],
             points=["Sàn có chức năng thanh toán khấu trừ, kê khai, nộp thay thuế cho người bán: hàng hóa 1% GTGT + 0,5% TNCN trên doanh thu gộp.",
                     "Tháng 8–9/2025: 63 sàn (55 trong nước, 8 nước ngoài) đã khai, nộp thay 1,07 nghìn tỷ đồng."],
             status="mid", status_text="Qua bài tóm tắt của LuatVietnam và EY; chưa đọc toàn văn.",
             sources=[("LuatVietnam", "https://luatvietnam.vn/tin-van-ban-moi/da-co-nghi-dinh-117-2025-nd-cp-ve-quan-ly-thue-doi-voi-kinh-doanh-tren-nen-tang-so-cua-ho-ca-nhan-186-102478-article.html"),
                      ("EY · 6/2025", "https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/tin-nhanh-tu-van-thue-nhan-su-thang-6-nam-2025-nghi-dinh-117-ve-quan-ly-thue-doi-voi-hoat-dong-kinh-doanh-tren-nen-tang-thuong-mai-dien-tu-nen-tang-so")]),
    ]),
    ("Ví điện tử và thanh toán", [
        dict(id="l-tt25", name="Thông tư 25/2025/TT-NHNN", sub="Sửa Thông tư 17/2024 về tài khoản thanh toán",
             dates=[("Ban hành", "31/08/2025"), ("Quy định tên tài khoản", "từ 01/03/2026")],
             points=["Tài khoản dùng cho kinh doanh phải đúng tên hộ trên Giấy chứng nhận đăng ký hộ kinh doanh; cấm bí danh, biệt danh.",
                     "MoMo cho biết Mã QR Doanh nghiệp là tài khoản nhận tiền đứng tên hộ theo quy định này (20/3/2026)."],
             status="mid", status_text="Qua bài tóm tắt của báo và LuatVietnam; chưa đọc toàn văn.",
             sources=[("Người Quan sát · 01/03/2026", "https://nguoiquansat.vn/tu-1-3-2026-ho-kinh-doanh-phai-mo-tai-khoan-dung-ten-dang-ky-276481.html"),
                      ("LuatVietnam", "https://luatvietnam.vn/linh-vuc-khac/diem-moi-ve-thong-tu-25-2025-tt-nhnn-ve-tai-khoan-thanh-toan-883-103982-article.html"),
                      ("MoMo · 20/03/2026", "https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-cap-nhat-moi-nhat-ve-giai-phap-nhan-tien-8587")]),
        dict(id="l-qd2345", name="Quyết định 2345/QĐ-NHNN", sub="Ngân hàng Nhà nước",
             dates=[("Hiệu lực", "01/07/2024")],
             points=["Chuyển tiền trực tuyến hoặc nạp ví trên 10 triệu đồng/lần, hoặc tổng trên 20 triệu đồng/ngày, phải xác thực sinh trắc học đối chiếu chip căn cước."],
             status="mid", status_text="Qua bài của báo và thư viện luật; chưa đọc toàn văn quyết định.",
             sources=[("Báo Pháp luật", "https://baophapluat.vn/chuyen-tien-bang-xac-thuc-sinh-trac-hoc-tu-172024-giam-thieu-cac-vu-lua-dao-chuyen-tien-qua-tai-khoan-post515757.html"),
                      ("Thư viện pháp luật", "https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/57646/chuyen-khoan-nap-tien-vi-dien-tu-tren-10-trieu-phai-xac-thuc-sinh-trac-hoc-tu-01-07-2024"),
                      ("LuatVietnam", "https://luatvietnam.vn/tin-van-ban-moi/tu-2024-chuyen-khoan-tren-10-trieu-dong-phai-xac-thuc-sinh-trac-hoc-186-96491-article.html")]),
        dict(id="l-tt41", name="Thông tư 40/2024/TT-NHNN, sửa bởi Thông tư 41/2025/TT-NHNN", sub="Dịch vụ trung gian thanh toán, ví điện tử",
             dates=[("Thông tư 41 hiệu lực", "05/11/2025")],
             points=["Ví điện tử không được cấp tín dụng hay trả lãi trên số dư (Khoản 5 Điều 25 Thông tư 40/2024).",
                     "Hạn mức 100 triệu đồng/tháng; 300 triệu đồng/tháng cho dịch vụ thiết yếu (điện, nước, viễn thông, học phí, viện phí, bảo hiểm, khoản vay đến hạn).",
                     "Từ 01/01/2026, mở ví phải xác thực sinh trắc học."],
             status="mid", status_text="Có link văn bản Thông tư 40 trên Thư viện pháp luật; nội dung Thông tư 41 qua VNBA và Tuổi Trẻ, chưa đọc toàn văn.",
             sources=[("Thư viện pháp luật (TT 40)", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-40-2024-TT-NHNN-huong-dan-hoat-dong-cung-ung-dich-vu-trung-gian-thanh-toan-615328.aspx"),
                      ("VNBA · 10/11/2025", "https://vnba.org.vn/vi/quy-dinh-moi-ve-vi-dien-tu--tang-an-toan--mo-rong-han-muc--siet-dinh-danh-19550.htm"),
                      ("Tuổi Trẻ · 10/11/2025", "https://tuoitre.vn/plo/tu-1-1-2026-muon-mo-vi-dien-tu-phai-xac-minh-thong-tin-sinh-trac-hoc-post880385.html"),
                      ("VietnamFinance · 24/08/2026", "https://vietnamfinance.vn/thu-phi-nguoi-dung-bai-toan-kho-cua-vi-dien-tu-d149537.html")]),
        dict(id="l-tt53", name="Thông tư 53/2026/TT-NHNN", sub="An toàn, quản lý rủi ro khi ứng dụng AI trong ngành ngân hàng",
             dates=[("Ký", "30/09/2026"), ("Hiệu lực", "15/11/2026")],
             points=["Phạm vi gồm cả tổ chức cung ứng dịch vụ trung gian thanh toán, tức các ví như MoMo.",
                     "AI tự động thực hiện thanh toán là rủi ro cao khi vượt 10 triệu đồng/lần hoặc 20 triệu đồng/ngày với cá nhân (50 triệu/lần, 100 triệu/ngày với tổ chức).",
                     "AI tự động quyết định tín dụng từ 50 triệu đồng trở lên là rủi ro cao.",
                     "Theo đưa tin, khách hàng phải có công cụ tạm dừng hoặc hủy quyền để AI tự động thanh toán; chi tiết này có thể lấy từ bản dự thảo."],
             status="mid", status_text="Chưa đọc toàn văn; nội dung qua Thị trường Tài chính Tiền tệ và VietnamPlus. Yêu cầu về giải thích và chuyển tiếp cần đối chiếu.",
             sources=[("Thị trường Tài chính Tiền tệ", "https://thitruongtaichinhtiente.vn/nhnn-ban-hanh-quy-dinh-ve-an-toan-quan-ly-rui-ro-khi-ung-dung-ai-trong-nganh-ngan-hang-86130.html"),
                      ("VietnamPlus", "https://www.vietnamplus.vn/ngan-hang-nha-nuoc-dat-nhieu-yeu-cau-khi-ngan-hang-ung-dung-ai-post1140808.vnp")]),
        dict(id="l-nd340", name="Nghị định 340/2025/NĐ-CP", sub="Xử phạt vi phạm hành chính, trong đó có mua bán, thuê, cho thuê tài khoản",
             dates=[("Hiệu lực", "09/02/2026")],
             points=["Phạt 100–150 triệu đồng khi mua, bán, thuê, cho thuê, mượn từ 1 đến dưới 10 tài khoản; 150–200 triệu đồng từ 10 tài khoản trở lên.",
                     "Có thể bị xử lý hình sự theo Điều 291 Bộ luật Hình sự (đến 7 năm tù).",
                     "Một bài CafeF khác ghi mức \u201cđến 250 triệu\u201d, có thể là mức với tổ chức; chưa đối chiếu."],
             status="low", status_text="Qua báo; các bài ghi mức phạt tối đa khác nhau và chưa đọc toàn văn nghị định.",
             sources=[("CafeF · 01/10/2026", "https://cafef.vn/mua-ban-tai-khoan-ngan-hang-coi-chung-ruoc-hoa-vao-than-188261001071944878.chn"),
                      ("CafeF · 05/08/2026", "https://cafef.vn/phat-den-250-trieu-dong-neu-nguoi-dung-tai-khoan-ngan-hang-co-hanh-vi-sau-188260805112154922.chn")]),
    ]),
    ("Dữ liệu cá nhân và AI", [
        dict(id="l-pdp", name="Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15", sub="Quốc hội",
             dates=[("Thông qua", "26/06/2025"), ("Hiệu lực", "01/01/2026")],
             points=["Điều 27: thông tin tài chính, ngân hàng, tín dụng phải áp dụng quy định về dữ liệu nhạy cảm.",
                     "Không được dùng thông tin tín dụng để chấm điểm, xếp hạng, đánh giá tín nhiệm khi chưa có sự đồng ý của chủ thể dữ liệu."],
             status="mid", status_text="Có link văn bản trên Thư viện pháp luật; nội dung lấy cùng bài của Bộ Công an và hãng luật.",
             sources=[("Bộ Công an", "https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/bao-ve-du-lieu-ca-nhan-trong-mot-so-hoat-dong-1754989261"),
                      ("Thư viện pháp luật", "https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so-91-2025-QH15-625628.aspx"),
                      ("Yen Nam Law", "https://yennamlawfirm.vn/luat-bao-ve-du-lieu-ca-nhan-91-2025-qh15/")]),
        dict(id="l-nd356", name="Nghị định 356/2025/NĐ-CP", sub="Hướng dẫn Luật Bảo vệ dữ liệu cá nhân; thay Nghị định 13/2023",
             dates=[("Ban hành", "31/12/2025"), ("Hiệu lực", "01/01/2026")],
             points=["Danh mục dữ liệu nhạy cảm được đưa tin là gồm thông tin tài khoản số, dữ liệu sinh trắc học và lịch sử giao dịch tài chính."],
             status="mid", status_text="Qua bài tóm tắt của EY, LuatVietnam và PwC; chưa đọc toàn văn.",
             sources=[("EY", "https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan"),
                      ("LuatVietnam", "https://luatvietnam.vn/legal-updates/new-features-of-decree-356-2025-compared-with-decree-13-2023-on-personal-data-protection-892-106712-article.html"),
                      ("PwC · 28/01/2026", "https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html")]),
        dict(id="l-ailaw", name="Luật Trí tuệ nhân tạo (134/2025/QH15)", sub="Quốc hội",
             dates=[("Thông qua", "10/12/2025"), ("Hiệu lực", "01/03/2026"), ("Chuyển tiếp", "18 tháng cho tài chính, y tế, giáo dục, đến khoảng 01/09/2027")],
             points=["Phân loại theo mức rủi ro; hệ thống rủi ro cao phải quản lý rủi ro, có hồ sơ kỹ thuật, nhật ký vận hành và đánh giá sự phù hợp trước khi triển khai.",
                     "Chatbot phải cho người dùng biết họ đang tương tác với AI; âm thanh, hình ảnh, video do AI tạo phải gắn nhãn máy đọc được."],
             status="low", status_text="Qua hãng luật và thư viện quốc tế. Số hiệu luật chỉ thấy ở nguồn thứ cấp; các nguồn mâu thuẫn về số tầng rủi ro (3 hay 4) và danh mục hệ thống rủi ro cao.",
             sources=[("Allen & Gledhill", "https://www.allenandgledhill.com/vn/publication/articles/32667/s-new-law-on-artificial-intelligence-risk-based-regulatory-framework-in-force-1-march-2026"),
                      ("Library of Congress · 03/04/2026", "https://www.loc.gov/item/global-legal-monitor/2026-04-03/vietnam-ai-law-takes-effect"),
                      ("Duane Morris · 03/03/2026", "https://blogs.duanemorris.com/vietnam/2026/03/03/vietnam-the-first-law-on-artificial-intelligence-what-you-must-know/"),
                      ("Vietnam Briefing", "https://www.vietnam-briefing.com/news/vietnams-ai-law-regulatory-milestone-business-implications.html/"),
                      ("CASRAI (số hiệu luật)", "https://casrai.org/guides/vietnam-ai-law-134-2025")]),
    ]),
]

LAW_PATTERNS = [
    ("l-nq198", r"(?:Nghị quyết|NQ)\s+198(?:/2025(?:/QH15)?)?"),
    ("l-nd141", r"(?:Nghị định|NĐ)\s+141(?:/2026(?:/NĐ-CP)?)?"),
    ("l-nd68", r"(?:Nghị định|NĐ)\s+68(?:/2026(?:/NĐ-CP)?)?"),
    ("l-nd68", r"(?:Thông tư|TT)\s+18(?:/2026(?:/TT-BTC)?)?"),
    ("l-nd70", r"(?:Nghị định|NĐ)\s+70(?:/2025(?:/NĐ-CP)?)?"),
    ("l-nd117", r"(?:Nghị định|NĐ)\s+117(?:/2025(?:/NĐ-CP)?)?"),
    ("l-nd356", r"(?:Nghị định|NĐ)\s+356(?:/2025(?:/NĐ-CP)?)?"),
    ("l-tt152", r"(?:Thông tư|TT)\s+152(?:/2025(?:/TT-BTC)?)?"),
    ("l-tt25", r"(?:Thông tư|TT)\s+25(?:/2025(?:/TT-NHNN)?)?"),
    ("l-tt53", r"(?:Thông tư|TT)\s+53(?:/2026(?:/TT-NHNN)?)?"),
    ("l-tt41", r"(?:Thông tư|TT)\s+4[01](?:/202[45](?:/TT-NHNN)?)?"),
    ("l-qd2345", r"(?:Quyết định|QĐ)\s+2345(?:/QĐ-NHNN)?"),
    ("l-pdp", r"Luật Bảo vệ dữ liệu cá nhân(?:\s+(?:số\s+)?91/2025(?:/QH15)?)?"),
    ("l-pdp", r"Luật BVDLCN"),
    ("l-ailaw", r"Luật Trí tuệ nhân tạo(?:\s+(?:số\s+)?134/2025(?:/QH15)?)?"),
    ("l-ailaw", r"Luật AI(?:\s+(?:số\s+)?134/2025(?:/QH15)?)?"),
    ("l-nd340", r"(?:Nghị định|NĐ)\s+340(?:/2025(?:/NĐ-CP)?)?"),
    ("l-nq198", r"(?<![\d/])198/2025(?:/QH15)?"),
    ("l-nd141", r"(?<![\d/])141/2026(?:/NĐ-CP)?"),
    ("l-nd68", r"(?<![\d/])68/2026(?:/NĐ-CP)?"),
    ("l-nd68", r"(?<![\d/])18/2026(?:/TT-BTC)?"),
    ("l-nd70", r"(?<![\d/])70/2025(?:/NĐ-CP)?"),
    ("l-nd117", r"(?<![\d/])117/2025(?:/NĐ-CP)?"),
    ("l-nd356", r"(?<![\d/])356/2025(?:/NĐ-CP)?"),
    ("l-tt152", r"(?<![\d/])152/2025(?:/TT-BTC)?"),
    ("l-tt25", r"(?<![\d/])25/2025(?:/TT-NHNN)?"),
    ("l-tt53", r"(?<![\d/])53/2026(?:/TT-NHNN)?"),
    ("l-tt41", r"(?<![\d/])(?:40/2024|41/2025)(?:/TT-NHNN)?"),
    ("l-pdp", r"(?<![\d/])91/2025(?:/QH15)?"),
    ("l-ailaw", r"(?<![\d/])134/2025(?:/QH15)?"),
]
LAW_RE = re.compile("|".join(f"(?P<g{i}>{p})(?![\\d/])" for i, (_, p) in enumerate(LAW_PATTERNS)))

EV = [("(suy luận)", "ev-inf", "suy luận"), ("(MoMo tự công bố)", "ev-self", "MoMo tự công bố"),
      ("(qua tóm tắt tìm kiếm)", "ev-snip", "qua tóm tắt tìm kiếm"), ("(kiến thức kỹ thuật chung)", "ev-tech", "kiến thức kỹ thuật chung")]

STATUS_LABEL = {"ok": "Đã đọc trang nguồn", "mid": "Qua bài tóm tắt", "low": "Chưa chắc chắn"}


def esc(t):
    return html.escape(t, quote=True)


def render_laws():
    out = []
    for group, items in LAWS:
        cards = []
        for d in items:
            dl = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in d["dates"])
            pts = "".join(f"<li>{esc(p)}</li>" for p in d["points"])
            srcs = "".join(f'<a class="src" href="{esc(u)}">{esc(l)}</a>' for l, u in d["sources"])
            cards.append(
                f'<article class="law" id="{d["id"]}"><h4>{esc(d["name"])}<span>{esc(d["sub"])}</span></h4>'
                f"<dl>{dl}</dl><ul>{pts}</ul>"
                f'<span class="status {d["status"]}">{esc(d["status_text"])}</span>'
                f'<div class="srcs">{srcs}</div></article>')
        out.append(f'<div class="law-group"><h3>{esc(group)}</h3><div class="laws">{"".join(cards)}</div></div>')
    return "".join(out)


def render_appendix_md():
    lines = [APPENDIX_MARK, "",
             "Bảng này liệt kê mọi văn bản pháp lý được dùng trong báo cáo, kèm ngày, nội dung được dùng, mức độ kiểm chứng và link nguồn. "
             "Mức độ: **Đã đọc trang nguồn** (cổng chính phủ, công báo, thư viện luật có nội dung văn bản); "
             "**Qua bài tóm tắt** (báo hoặc hãng luật, chưa đọc toàn văn); **Chưa chắc chắn** (chỉ thấy qua đoạn trích tìm kiếm, hoặc nguồn mâu thuẫn).", ""]
    for group, items in LAWS:
        lines += [f"### {group}", ""]
        for d in items:
            dates = "; ".join(f"{k}: {v}" for k, v in d["dates"])
            lines.append(f"**{d['name']}** ({d['sub']}). {dates}.")
            lines.append("")
            for p in d["points"]:
                lines.append(f"- {p}")
            lines.append(f"- Mức độ: {STATUS_LABEL[d['status']]}. {d['status_text']}")
            lines.append("- Nguồn: " + "; ".join(f"[{l}]({u})" for l, u in d["sources"]))
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def transform_text(text):
    """Link legal instruments and tag evidence labels in a text node (already HTML-escaped)."""
    def law_sub(m):
        idx = int(m.lastgroup[1:])
        return f'<a class="law-ref" href="#{LAW_PATTERNS[idx][0]}">{m.group(0)}</a>'
    text = LAW_RE.sub(law_sub, text)
    for raw, cls, label in EV:
        text = text.replace(raw, f'<span class="ev {cls}">{label}</span>')
    return text


def process_html(body):
    # Walk tags; transform only text outside <a> and outside headings.
    parts = re.split(r"(<[^>]+>)", body)
    in_a = 0
    in_h = 0
    for i, p in enumerate(parts):
        if p.startswith("<"):
            t = p.lower()
            if re.match(r"<a[\s>]", t):
                in_a += 1
            elif t.startswith("</a"):
                in_a -= 1
            elif re.match(r"<h[1-6][\s>]", t):
                in_h += 1
            elif re.match(r"</h[1-6]", t):
                in_h -= 1
            continue
        if in_a == 0 and in_h == 0 and p.strip():
            parts[i] = transform_text(p)
    return "".join(parts)


def main():
    md = REPORT.read_text(encoding="utf-8")
    body_md = md.split(APPENDIX_MARK)[0].rstrip() + "\n"
    # Refresh the appendix in the markdown report so the repo copy carries the same sources.
    REPORT.write_text(body_md + "\n" + render_appendix_md(), encoding="utf-8")

    art = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", "--wrap=none"], input=body_md,
                         capture_output=True, text=True, check=True).stdout
    # Drop the H1 (the cover carries it) and open the intro with a "Tóm tắt" heading.
    art = re.sub(r"<h1[^>]*>.*?</h1>\s*", '<h2 id="r0">Tóm tắt</h2>\n', art, count=1, flags=re.S)
    toc = []
    counters = {"h2": 0, "h3": 0}

    def head_sub(m):
        tag, inner = m.group(1), m.group(3)
        text = re.sub(r"<[^>]+>", "", inner)
        if tag == "h2":
            if m.group(0).startswith('<h2 id="r0"'):
                hid = "r0"
            else:
                counters["h2"] += 1
                counters["h3"] = 0
                hid = f"r{counters['h2']}"
            toc.append([hid, text, []])
        else:
            counters["h3"] += 1
            hid = f"r{counters['h2']}-{counters['h3']}"
            toc[-1][2].append((hid, text))
        return f'<{tag} id="{hid}">{inner}</{tag}>'

    art = re.sub(r"<(h[23])([^>]*)>(.*?)</h[23]>", head_sub, art, flags=re.S)
    art = re.sub(r"<table>", '<div class="table-wrap"><table>', art)
    art = art.replace("</table>", "</table></div>")
    art = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', art)
    art = process_html(art)

    def toc_html():
        items = []
        for hid, text, subs in toc:
            sub = ""
            if subs:
                sub = "<ol>" + "".join(f'<li><a href="#{s}">{t}</a></li>' for s, t in subs) + "</ol>"
            items.append(f'<li><a href="#{hid}">{text}</a>{sub}</li>')
        return "<ol>" + "".join(items) + "</ol>"

    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("{{LAWS}}", render_laws()).replace("{{TOC}}", toc_html()).replace("{{ARTICLE}}", art)
    page = re.sub(r'<a class="src" href="(https?://[^"]+)"', r'<a class="src" href="\1" target="_blank" rel="noopener noreferrer"', page)
    OUT.write_text(page, encoding="utf-8")

    refs = re.findall(r'class="law-ref" href="#([^"]+)"', page)
    ids = set(re.findall(r'<article class="law" id="([^"]+)"', page))
    missing = sorted(set(refs + re.findall(r'href="#(l-[^"]+)"', page)) - ids)
    print("law refs:", len(refs), "unique:", sorted(set(refs)), "missing targets:", missing)
    print("toc h2:", len(toc), "bytes:", len(page.encode("utf-8")))


main()
