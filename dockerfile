# FROM mysql:latest

# # 초기화 SQL 파일을 실행할 디렉토리로 이동
# WORKDIR /docker-entrypoint-initdb.d

# # 초기화 SQL 파일 복사
# COPY ./security_logs.sql .
# COPY ./users.sql .

# # 환경 변수 설정
# ENV MYSQL_ROOT_PASSWORD=!pyree2023
# ENV MYSQL_DATABASE=logs


# MySQL 최신 버전을 기반으로 하는 Docker 이미지를 사용
FROM mysql:latest

# MySQL 데이터베이스 초기화 시 실행될 SQL 스크립트가 위치한 디렉토리로 작업 디렉토리 설정
WORKDIR /docker-entrypoint-initdb.d

# 호스트 시스템에서 컨테이너의 현재 작업 디렉토리로 SQL 스크립트 파일들 복사
COPY ./security_logs.sql .
COPY ./users.sql .

# MySQL 컨테이너가 3306 포트를 사용하도록 설정 (선택적)
EXPOSE 3306

