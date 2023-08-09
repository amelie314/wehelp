from flask import Flask, render_template, request, redirect, session, url_for

import mysql.connector

app = Flask(__name__)

# Database configuration
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
        
        # Check if username already exists
        cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return redirect(url_for('error', message='帳號已經被註冊'))
        
        # Insert new user into database
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        db.commit()
        
        return redirect(url_for('index'))
    
@app.route('/sign_in', methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    
    cursor = db.cursor()
    
    # Check if username and password match
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        session['authenticated'] = True  # Store user authentication state in session
        session['user_id'] = user[0]  # Store user ID in session
        session['username'] = user[2]  # Store username in session
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

@app.route('/member')
def member():
    # Check if the user is authenticated before showing the success page
    if session.get('authenticated'):
        return render_template('member.html', username=session.get('username'))
    else:
        # Redirect to the home page if not signed in
        return redirect(url_for('index'))
    
@app.route('/error')
def error():
    error_message = request.args.get('message')
    return render_template('error.html', error_message=error_message)

@app.route('/signout', methods=['GET'])
def signout():
    # Clear the user state in the session when signing out
    session['authenticated'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
