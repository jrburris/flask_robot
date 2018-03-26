from flask import Flask
from flask import render_template   # , Response


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/forward")
def forward():
    return 'Forward'


@app.route("/reverse")
def reverse():
    return 'Reverse'


@app.route("/spin_left")
def spin_left():
    return 'Spin Left'


@app.route("/spin_right")
def spin_right():
    return 'Spin Right'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5010, threaded=True)
