from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
