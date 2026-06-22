# BÁO CÁO THỰC HÀNH KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM WEBDRIVER
## 1. Thông tin bài thực hành
Công cụ: Selenium WebDriver

Ngôn ngữ: Python

Framework kiểm thử: Pytest

Website kiểm thử: SauceDemo

Trình duyệt: Google Chrome

## 2. Mục tiêu
Bài thực hành nhằm tìm hiểu cách Selenium WebDriver điều khiển trình duyệt và xây dựng các ca kiểm thử tự động cho một website. Cụ thể:

Cài đặt và cấu hình môi trường Selenium với Python.

Sử dụng các phương thức tìm kiếm phần tử: id, class name, xpath.

Thực hiện các thao tác cơ bản: nhập liệu, nhấn nút, chờ đợi phần tử với WebDriverWait.

Tổ chức các test case với Pytest và kiểm tra kết quả mong đợi.

## 3. Tài liệu tham khảo
Selenium with Python – Official Documentation

Selenium Waits – Explicit Wait

Pytest Documentation

SauceDemo Demo Site

##4. Cấu trúc thư mục dự án
text
selenium-test-automation/
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_add_to_cart.py
├── requirements.txt
└── README.md
tests/: chứa các file test case.

requirements.txt: danh sách các thư viện cần cài đặt.

README.md: báo cáo thực hành (file này).

##5. Các test case
Mã	Chức năng	Các bước thực hiện	Kết quả mong đợi
TC01	Đăng nhập thành công	1. Mở trang đăng nhập
2. Nhập username standard_user
3. Nhập password secret_sauce
4. Nhấn nút Login	Chuyển đến trang sản phẩm (URL chứa /inventory)
TC02	Kiểm tra danh sách sản phẩm	1. Đăng nhập thành công
2. Kiểm tra số lượng sản phẩm hiển thị	Có ít nhất 1 sản phẩm trong danh sách
TC03	Thêm sản phẩm vào giỏ hàng	1. Đăng nhập
2. Nhấn nút "Add to cart" của sản phẩm đầu tiên
3. Xem biểu tượng giỏ hàng	Biểu tượng giỏ hàng hiển thị số 1
##6. Cài đặt và chạy kiểm thử
Yêu cầu hệ thống
Python 3.10 trở lên

Google Chrome (phiên bản mới nhất)

Kết nối Internet (để tải WebDriver tự động)

Bước 1: Clone repository
bash
git clone <URL_REPOSITORY>
cd selenium-test-automation
Bước 2: Tạo môi trường ảo (khuyến nghị)
bash
python -m venv .venv
# Kích hoạt môi trường:
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Bước 3: Cài đặt các thư viện
bash
pip install -r requirements.txt
Bước 4: Chạy toàn bộ test
bash
pytest tests/
Kết quả sẽ hiển thị trên terminal. Các test đều được kỳ vọng PASSED.

Bước 5: (Tùy chọn) Chạy test với chế độ hiển thị trình duyệt
Mặc định, các test sẽ chạy ở chế độ headless (không hiển thị trình duyệt). Để quan sát trình duyệt thực tế, bạn có thể sửa code: trong mỗi file test, thay webdriver.Chrome() thành webdriver.Chrome() (không thêm tham số headless) hoặc cài biến môi trường phù hợp.

##7. Kết quả thực hiện
Khi chạy lệnh pytest tests/, kết quả mong đợi:

text
============================= test session starts ==============================
tests/test_login.py::TestLogin::test_login_success PASSED
tests/test_search.py::TestSearch::test_search_products PASSED
tests/test_add_to_cart.py::TestAddToCart::test_add_first_item_to_cart PASSED
============================== 3 passed in 15.23s ==============================
Nhận xét:

Cả ba test case đều thực thi thành công, đáp ứng đúng kịch bản kiểm thử.

Thời gian thực thi trung bình khoảng 15 giây.

##8. Kiến thức thu được
Qua bài thực hành, tôi đã nắm được:

Quy trình viết một test case tự động với Selenium: Arrange – Act – Assert.

Cách khởi tạo và đóng WebDriver một cách an toàn bằng setup và teardown trong Pytest.

Cách sử dụng WebDriverWait để chờ đợi phần tử xuất hiện, tránh lỗi không tìm thấy phần tử.

Tầm quan trọng của việc chọn selector chính xác và ưu tiên dùng id thay vì xpath.

Cách tổ chức các test case độc lập, dễ dàng mở rộng và bảo trì.

##9. Hạn chế và hướng phát triển
Hạn chế
Chưa áp dụng mô hình Page Object Model (POM) để tái sử dụng code.

Chưa hỗ trợ kiểm thử đa trình duyệt.

Chưa có báo cáo kết quả chi tiết (dạng HTML).

Hướng phát triển
Tái cấu trúc dự án theo POM để giảm trùng lặp và dễ bảo trì.

Tích hợp thêm các test case cho chức năng đăng xuất, xóa sản phẩm khỏi giỏ.

Chạy tự động trên nhiều trình duyệt (Chrome, Firefox, Edge).

Tạo báo cáo HTML với pytest-html và chụp ảnh màn hình khi test thất bại.

Tích hợp CI/CD với GitHub Actions để tự động chạy test mỗi khi có thay đổi mã nguồn.
