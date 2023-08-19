from flask import Flask, render_template, request, redirect, session, url_for, jsonify

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
    # if request.method == 'POST':
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
    
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        session['authenticated'] = True  
        session['user_id'] = user['id'] 
        session['username'] = user['username'] 
        session['name'] = user['name']
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

@app.route('/error')
def error():
    error_message = request.args.get('message')
    return render_template('error.html', error_message=error_message)

@app.route('/signout', methods=['GET'])
def signout():
    session['authenticated'] = False
    return redirect(url_for('index'))


@app.route('/create_message', methods=['POST'])
def create_message():
    if session.get('authenticated'):
        user_id = session.get('user_id')
        content = request.form.get('content')
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
        db.commit()
        
        return redirect(url_for('member'))
    else:
        return redirect(url_for('index'))

@app.route('/member')
def member():
    if session.get('authenticated'):
        
        cursor = db.cursor(dictionary=True)

        # 修改的 SQL 查詢，新增 message.id, message.member_id 和 message.time
        query = """
        SELECT message.id, member.name, message.content, message.member_id, message.time
        FROM message
        INNER JOIN member ON message.member_id = member.id
        ORDER BY message.time DESC
        """

        cursor.execute(query)

        messages = []
        for message_row in cursor.fetchall():
            message = {
                'id': message_row['id'],
                'name': message_row['name'], 
                'content': message_row['content'],
                'member_id': message_row['member_id'],
                'time': message_row['time'].strftime('%Y-%m-%d %H:%M:%S')  # 格式化時間
            }
            messages.append(message)
        
        return render_template('member.html', username=session.get('username'),messages=messages, name=session.get('name'))
    else:
        return redirect(url_for('index'))


@app.route('/delete_message', methods=['POST'])
def delete_message():
    if session.get('authenticated'):
        message_id = request.form.get('message_id')
        
        cursor = db.cursor()
        cursor.execute("DELETE FROM message WHERE id = %s", (message_id,))
        db.commit()
        
        return redirect(url_for('member'))
    else:
        return redirect(url_for('index'))
    
@app.route("/api/member", methods=["GET"])
def get_member_info():
    # 從查詢參數中獲取 username
    username = request.args.get("username")
    
    if not username:
        return jsonify({"error": "Username parameter is required!"}), 400

    cursor = db.cursor(dictionary=True)
    
    # 查詢資料庫中的會員資料
    cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    member = cursor.fetchone()

    if not member:
        return jsonify({"error": "Member not found!"}), 404

    return jsonify({
        "data": {
            "id": member["id"],
            "name": member["name"],
            "username": member["username"]
        }
    })
@app.route('/api/member', methods=['PATCH'])
def update_member_name():
    if not session.get('authenticated'):
        return jsonify(error=True), 401  #未認證

    # 從request body中獲取新的姓名
    data = request.get_json()
    new_name = data.get('name', '')
    session['name'] = new_name

    if not new_name:
        return jsonify(error=True), 400  #錯誤的請求

    try:
        cursor = db.cursor()
        cursor.execute("UPDATE member SET name=%s WHERE id=%s", (new_name, session['user_id']))
        db.commit()
        return jsonify(ok=True)
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return jsonify(error=True), 500  #伺服器錯誤



if __name__ == '__main__':
    app.run(debug=True, port=3000)