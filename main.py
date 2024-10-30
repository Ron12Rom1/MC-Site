import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Admin users with their passwords
admin_users_list = {'Ron12Rom1': '12345'}

# Global server status
server_status = 'Offline'

@app.route("/Home", methods=['GET', 'POST'])
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
        if username in admin_users_list and admin_users_list[username] == password:
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
        return render_template('admin.html', server_status=server_status, admin_users_list=admin_users_list.keys())

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

@app.route("/profile/<user>", methods=['GET', 'POST'])
def profile(user):
    if 'username' not in session:
        return redirect('/admin/login')
    if request.method == 'POST':
        if request.form.get(f'delete_{user}') == 'Delete User':
            print(f"Delete User pressed: {user}")

    if user not in admin_users_list:
        return "User does not exist"
    return render_template('user.html', user=user)

@app.route("/delete/<user>", methods=['GET', 'POST'])
def delete_user(user):
    if 'username' not in session:
        return redirect('/admin/login')
    admin_users_list.pop(user)
    return redirect('/admin')

@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    if 'username' not in session:
        return redirect('/admin/login')
    if request.method == 'POST':
        username = request.form.get('username')
        admin_users_list[username] = "N/A"
        print(admin_users_list)
        return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 6969)))
