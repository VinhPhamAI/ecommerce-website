# Lala Books

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-563D7C?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-CC2927?logo=microsoft-sql-server&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />
</p>

## About this Project:

Lalabooks là một nền tảng trực tuyến dành cho những người yêu sách, cung cấp một bộ sưu tập phong phú các đầu sách đến từ nhiều thể loại khác nhau.

Hệ thống được xây dựng bằng Django, với dữ liệu  chứa tập dữ liệu với hơn 5000 phim và 200000 thông tin về khách hàng và rating thu thập từ đa dạng nguồn dữ liệu.

Hệ thống cho phép người dùng đăng nhập, đăng ký, xem các sách từ nhiều thể loại, đăng bán một sách mới, thanh toán và xem lịch sử thanh toán. Với giao diện được cung cấp dựa trên html, CSS và sử dụng cơ sở dữ liệu PostgreSQL. Đồng thời hệ thống có bao gồm đề xuất dựa trên rating và các sách được xem của người dùng.

## How to run a code:

```
$ git clone https://github.com/VinhPhamAI/ecommerce-website

$ cd ecommerce_app

```

Tạo một file .env trong thư mục ecommerce_app để thiết lập tất cả các thư viện cần thiết như dưới đây:

```
POSTGRES_PASSWORD=your_psql_password
POSTGRES_USER=your_psql_username
POSTGRES_DB=ecommerce_database
SECRET_KEY = 'django-insecure-@lhb-d4u!g$lh%tokwbs5m6qr2)bni&=&ku8(vf_*gq%+b^u5%'
DJANGO_SUPERUSER_USERNAME=your_username
DJANGO_SUPERUSER_PASSWORD=your_password
DJANGO_SUPERUSER_EMAIL=your_email@gmail.com
```

Chạy lệnh dưới để xây dựng Docker Image và tạo các container Docker từ image đó 

```
$ docker compose up --build
```

Mở http://localhost:8000 và dùng thử website của chúng tôi.

## License

<a href="https://github.com/fl4viooliveira/django_ecommerce/blob/master/LICENSE">
    <img alt="NPM" src="https://img.shields.io/npm/l/license?style=for-the-badge">
</a>&nbsp;&nbsp;
