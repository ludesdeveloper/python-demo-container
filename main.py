from flask import Flask
from sys import argv

app = Flask(__name__)


@app.route("/"+argv[1])
def hello_world():
    return argv[1]


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
