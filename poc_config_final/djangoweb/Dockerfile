FROM python:3.11.3

WORKDIR /usr/src/app/djangoweb

COPY ${PWD}/djangoweb/puddle/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY djangoweb .

WORKDIR /usr/src/app/djangoweb/puddle

EXPOSE 80

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:80"]