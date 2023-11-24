# from flask import Flask, render_template
# import pymysql

# app = Flask(__name__)

# # MySQL 데이터베이스 연결
# db = pymysql.connect(
#     host='mysql',
#     user='root',
#     password='1111',
#     database='logs', 
#     charset='utf8'
# )

# @app.route("/")
# def main():
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM security_logs')
#     data = cursor.fetchall()
#     return render_template('index.html', data=data)

# if __name__ == "__main__":
#     app.run()


# import pymysql

# # # MySQL 연결 설정
# # db_host = "mysql"  # 도커 컨테이너 이름(mysql)로 연결
# # db_user = "root"
# # db_password = "1111"
# # db_database = "logs"

# # MySQL 데이터베이스 연결
# try:
#     db = pymysql.connect(
#         host='172.20.0.3',  # 변경된 부분 (정확한 정보를 넣어야 된다, mysqld (localhost라는 정의 자체, docker mysql 내부의 ip 주소로 접속해서 시도해보기)) 172.30.0.6
#         #docker ip 주소 확인: docker network inspect (172.18.0.5)
#         user='root',
#         password='1111',
#         database='logs',  # 'db'를 'database'로 수정
#         charset='utf8'
#     )
    
#     # 연결이 정상적으로 되었을 때 실행할 코드
#     # 예시: cursor = db.cursor()
#     # 예시: cursor.execute("SELECT * FROM your_table")
#     # 예시: data = cursor.fetchall()
#     # 예시: print(data)

# except pymysql.MySQLError as e:
#     print(f"Error connecting to MySQL: {e}")
#     db = None  # 에러 발생 시 db 변수를 None으로 설정

# finally:
#     if db:
#         db.close()  # 연결 종료



# 멘토님 코드
# !/usr/bin/env python3
# import pymysql
# import pprint
# try:
#     db = pymysql.connect(
#         host='mysql',  # 변경된 부분
#         user='root',
#         password='1111',
#         database='mysql',  # 'db'를 'database'로 수정
#         charset='utf8'
#     )
#     # 연결이 정상적으로 되었을 때 실행할 코드
#     # 예시: cursor = db.cursor()
#     # 예시: cursor.execute("SELECT * FROM your_table")
#     # 예시: data = cursor.fetchall()
#     # 예시: print(data)
# except pymysql.MySQLError as e:
#     print(f"Error connecting to MySQL: {e}")
#     db = None  # 에러 발생 시 db 변수를 None으로 설정
# pprint.pprint(db)


# # 4차 시도
# import pymysql
# import pprint
# import os

# try:
#     db_host = os.environ.get('DB_HOST', 'mysql')
#     db_user = os.environ.get('DB_USER', 'root')
#     db_password = os.environ.get('DB_PASSWORD', '1111')
#     db_database = os.environ.get('DB_DATABASE', 'logs')

#     db = pymysql.connect(
#         host=db_host,
#         user=db_user,
#         password=db_password,
#         database=db_database,
#         charset='utf8'
#     )

#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM security_logs")
#     data = cursor.fetchall()
#     print(data)

# except pymysql.MySQLError as e:
#     print(f"Error connecting to MySQL: {e}")
#     db = None  # 에러 발생 시 db 변수를 None으로 설정

# pprint.pprint(db)



# # 5차 시도
# import pymysql
# import os

# try:
#     db_host = os.environ.get('DB_HOST', 'mysql')
#     db_user = os.environ.get('DB_USER', 'root')
#     db_password = os.environ.get('DB_PASSWORD', '1111')
#     db_database = os.environ.get('DB_DATABASE', 'logs')

#     db = pymysql.connect(
#         host=db_host,
#         user=db_user,
#         password=db_password,
#         database=db_database,
#         charset='utf8'
#     )

#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM security_logs")
#     data = cursor.fetchall()
#     print(data)

# except pymysql.MySQLError as e:
#     print(f"Error connecting to MySQL: {e}")
#     db = None  # 에러 발생 시 db 변수를 None으로 설정

# 6차 시도 (멘토님 코드)
import pymysql
import pprint
import os
import time

try:
    db_host = os.environ.get('DB_HOST', 'mysql')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '1111')
    db_database = os.environ.get('DB_DATABASE', 'logs')
    
    time.sleep(10)  # 여기서 10초 대기합니다.
    
    db = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    
    if db:
        print("Successfully connected to MySQL!")
        # 필요한 작업 수행
    
except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")
    db = None  # 에러 발생 시 db 변수를 None으로 설정
