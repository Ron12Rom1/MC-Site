import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

admin_users = {'Ron12Rom1': '12345'}

global server_status
server_status = 'Offline'  # Initial server status

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html', status=server_status)

@app.route("/ron12rom1")
def main():
    return "Welcome Ron12Rom1"

@app.route("/admin/login", methods=['GET', 'POST'])
def login():
    login_failed = False
    if request.method == 'GET':
        return render_template('login.html', login_failed=login_failed)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in admin_users and admin_users[username] == password:
            session['username'] = username
            print("Login Successful")
            return redirect('/admin')
        else:
            login_failed = True
            print("Login Failed")
            return render_template('login.html', login_failed=login_failed)

@app.route("/admin", methods=['GET', 'POST'])
def admin_panel():
    global server_status  # Declare server_status as global to modify it
    if 'username' not in session:
        return redirect('/admin/login')

    if request.method == 'GET':
        return render_template('admin.html', server_status=server_status)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Turn Server On':
            server_status = 'Online'
            print("Server turned on")
        elif action == 'Turn Server Off':
            server_status = 'Offline'
            print("Server turned off")
        elif action == 'Make custom message':
            message = request.form.get('message')
            server_status = message
            print(f"Custom message: {message}")

        return redirect('/admin')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 6969)))

