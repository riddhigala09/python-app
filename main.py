from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!! Nice to meet you.</p>"

if __name__ == '__main__':
    app.run (host="0.0.0.0", port=3000)
