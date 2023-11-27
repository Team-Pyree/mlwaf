FROM mysql:latest

# 초기화 SQL 파일을 실행할 디렉토리로 이동
WORKDIR /docker-entrypoint-initdb.d

# 초기화 SQL 파일 복사
COPY ./security_logs.sql .

# 환경 변수 설정
ENV MYSQL_ROOT_PASSWORD=!pyree2023
ENV MYSQL_DATABASE=logs