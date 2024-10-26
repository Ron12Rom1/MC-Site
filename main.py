import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

server_status = False

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
    return "Welcom Ron12Rom1"

@app.route("/admin", methods=['GET', 'POST'])
def admin_panel():
    global server_status
    if request.method == 'GET':
        return render_template('admin.html')

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Turn Server On':
            server_status = True
        elif action == 'Turn Server Off':
            server_status = False
        return redirect('/admin')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

