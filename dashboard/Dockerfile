FROM python:3.11.3
WORKDIR /usr/src/app

COPY ./dashboard/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./dashboard .

# app.py가 있는 디렉토리 내부에서 static 디렉토리를 복사합니다.
COPY ./dashboard/static /usr/src/app/dashboard/static

EXPOSE 80
CMD ["python", "app.py"]
