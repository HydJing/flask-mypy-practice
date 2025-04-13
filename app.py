from typing import Dict

from flask import Flask, jsonify

app: Flask = Flask(__name__)


@app.route("/")
def hello_world() -> Dict[str, str]:
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    app.run(debug=True)
