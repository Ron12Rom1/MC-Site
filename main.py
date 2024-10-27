import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

server_status = False  # Initial server status

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html', status=server_status)

    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Ron12Rom1' and password == 'Ron1234509876':
            print("Login Successful")
            return redirect('/ron12rom1')
        else:
            print("Login Failed")
            return redirect('/')

@app.route("/ron12rom1")
def main():
    return "Welcome Ron12Rom1"

@app.route("/admin", methods=['GET', 'POST'])
def admin_panel():
    global server_status
    if request.method == 'GET':
        return render_template('admin.html', server_status=server_status)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Turn Server On':
            server_status = True
            print("Server turned on")
        elif action == 'Turn Server Off':
            server_status = False
            print("Server turned off")
        return redirect('/admin')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 2727)))
