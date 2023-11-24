FROM python:3.11.3
WORKDIR /usr/src/app

COPY ${PWD}/dashboard/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY dashboard .

EXPOSE 80
CMD ["python", "app.py"]
