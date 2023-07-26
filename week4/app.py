from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the form data
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')

        # Verify username and password
        if not username or not password:
            # Redirect to the error page with "Please enter username and password" message
            error_message = "Please enter username and password"
            return redirect(url_for('error', message=error_message))
        elif username == "test" and password == "test":
            # Store the user state in the session
            session['username'] = username
            session['authenticated'] = True
            # Redirect to the success page if verification is successful
            return redirect(url_for('success'))
        else:
            # Redirect to the error page with "Username or password is not correct" message
            error_message = "Username or password is not correct"
            return redirect(url_for('error', message=error_message))

    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def signin():
    # This route is used to handle the form submission, but we have already
    # handled it in the home() function, so we can leave this empty.
    pass

@app.route('/member')
def success():
    # Check if the user is authenticated before showing the success page
    if session.get('authenticated'):
        return render_template('member.html', username=session.get('username'))
    else:
        # Redirect to the home page if not signed in
        return redirect(url_for('home'))

@app.route('/error')
def error():
    error_message = request.args.get('message')
    return render_template('error.html', error_message=error_message)

@app.route('/signout', methods=['GET'])
def signout():
    # Clear the user state in the session when signing out
    session['authenticated'] = False
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/square/<int:number>')
def squared_number(number):
    squared = number ** 2
    return render_template('square.html', number=number, squared=squared)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
