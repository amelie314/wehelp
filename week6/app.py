from flask import Flask, render_template, request, redirect, session, url_for

import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="website"
)

app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return redirect(url_for('error', message='帳號已經被註冊'))
        
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        db.commit()
        
        return redirect(url_for('index'))
    
@app.route('/sign_in', methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        session['authenticated'] = True  
        session['user_id'] = user[0] 
        session['username'] = user[2] 
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

@app.route('/member')
def member():
    if session.get('authenticated'):
        return render_template('member.html', username=session.get('username'))
    else:
        return redirect(url_for('index'))
    
@app.route('/error')
def error():
    error_message = request.args.get('message')
    return render_template('error.html', error_message=error_message)

@app.route('/signout', methods=['GET'])
def signout():
    session['authenticated'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
