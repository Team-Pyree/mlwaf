from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def connect_to_mysql():
    try:
        return pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=3306,
            user=os.getenv("DB_PORT"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
            charset='utf8'
        )
    except pymysql.MySQLError as e:
        print(f"MySQL 연결 오류: {e}")
        return None

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('비밀번호가 일치하지 않습니다.')
            return redirect(url_for('signup'))

        hashed_password = hash_password(password)

        db = connect_to_mysql()
        if db:
            try:
                with db.cursor() as cursor:
                    sql = "INSERT INTO users (fullname, email, phone, password) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (fullname, email, phone, hashed_password))
                    db.commit()
                    flash("회원가입에 성공하였습니다.")
                    return redirect(url_for('login'))
            except pymysql.MySQLError as e:
                db.rollback()
                flash(f"회원가입 실패: {e}")
            finally:
                db.close()

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)

        db = connect_to_mysql()
        if db:
            try:
                with db.cursor(pymysql.cursors.DictCursor) as cursor:
                    sql = "SELECT * FROM users WHERE email = %s AND password = %s"
                    cursor.execute(sql, (username, hashed_password))
                    result = cursor.fetchone()
                    if result:
                        session['username'] = result['fullname']
                        session['login_successful'] = True  # 로그인 성공 플래그 설정
                        return redirect(url_for('index'))
                    else:
                        flash('잘못된 사용자 이름 또는 비밀번호입니다.')
            finally:
                db.close()

    return render_template('login.html')


@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if session.pop('login_successful', False):
        flash("로그인에 성공하였다")  # 로그인 성공 메시지 설정

    db = connect_to_mysql()
    if db:
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM security_logs")
                data = cursor.fetchall()
            return render_template('index.html', data=data)
        except pymysql.MySQLError as e:
            print(f"MySQL 쿼리 오류: {e}")
            return "MySQL 연결 중"
        finally:
            db.close()
    else:
        return "MySQL 연결 중"
    
@app.route('/logout')
def logout():
    session.pop('username', None)  # 세션에서 'username' 제거
    flash("성공적으로 로그아웃되었습니다.")
    return redirect(url_for('login'))  # 로그인 페이지로 리디렉션


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9093, debug=True)
