import datetime
import json
import os

from flask import Flask

PATH_MAIN = os.path.dirname(os.path.abspath(__file__))
RES_PATH = os.path.join(PATH_MAIN, "resources")

app = Flask(__name__)

@app.route('/')
def start():
    with open(os.path.join(RES_PATH, "data.json")) as f:
        data_resource = json.loads(f.read()).get("place")
    return f"{data_resource} - {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
