from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# MySQL 데이터베이스 연결
db = pymysql.connect(
    host='localhost',
    user='root',
    password='1111',
    database='logs', 
    charset='utf8'
)

@app.route("/")
def main():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM security_logs')
    data = cursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
