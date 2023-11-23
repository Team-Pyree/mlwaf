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


import pymysql

# MySQL 연결 설정
db_host = "mysql"  # 도커 컨테이너 이름(mysql)로 연결
db_user = "root"
db_password = "1111"
db_database = "logs"

# MySQL 데이터베이스 연결
try:
    db = pymysql.connect(
        host='localhost',  # 변경된 부분
        user='root',
        password='1111',
        database='logs',  # 'db'를 'database'로 수정
        charset='utf8'
    )
    
    # 연결이 정상적으로 되었을 때 실행할 코드
    # 예시: cursor = db.cursor()
    # 예시: cursor.execute("SELECT * FROM your_table")
    # 예시: data = cursor.fetchall()
    # 예시: print(data)

except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")
    db = None  # 에러 발생 시 db 변수를 None으로 설정

finally:
    if db:
        db.close()  # 연결 종료
