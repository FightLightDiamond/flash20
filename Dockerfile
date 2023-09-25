# Sử dụng hình ảnh Python 3.11
FROM python:3.11

# Đặt thư mục làm việc
WORKDIR /www

# Sao chép tệp requirements.txt vào container
COPY requirements.txt requirements.txt

# Cài đặt Flask và các dependencies
RUN pip install -r requirements.txt

# Sao chép mã nguồn ứng dụng vào container
COPY . /www
#
# Expose cổng 5000
EXPOSE 5000

ENV FLASK_APP=app

#CMD ["python", "app.py"]
CMD ["python", "app.py"]