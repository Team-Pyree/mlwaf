from flask import Flask, render_template
import pymysql

app = Flask(__name__)

def connect_to_mysql():
    try:
        db = pymysql.connect(
            host='mysql',
            port=3306,
            user='root',
            password='!pyree2023',
            database='logs',
            charset='utf8'
        )
        return db
    except pymysql.MySQLError as e:
        print(f"MySQL 연결 오류: {e}")
        return None

@app.route('/')
def index():
    db = connect_to_mysql()

    if db:
        try:
            cursor = db.cursor(pymysql.cursors.DictCursor)  # 딕셔너리 커서로 변경하여 컬럼명 기반으로 데이터에 접근
            cursor.execute("SELECT * FROM security_logs")
            data = cursor.fetchall()
            db.close()
            return render_template('index.html', data=data)
        except pymysql.MySQLError as e:
            print(f"MySQL 쿼리 오류: {e}")
            db.close()
            return f"MySQL 쿼리 오류: {e}"
    else:
        return "MySQL 연결 중"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9093, debug=True)



