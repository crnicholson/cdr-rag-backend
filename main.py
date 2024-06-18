from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route("/api/time", methods=["GET"])
def return_home():
    return jsonify({"time": str(datetime.now())})


if __name__ == "__main__":
    app.run(debug=True, port=7359)
