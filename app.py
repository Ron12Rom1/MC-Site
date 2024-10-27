from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Initialize the boolean variable
bool_value = False

@app.route('/')
def index():
    return render_template("index.html", bool_value=bool_value)

@app.route('/toggle', methods=['POST'])
def toggle():
    global bool_value
    bool_value = not bool_value  # Toggle the boolean
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
