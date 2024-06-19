from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from openai import OpenAI


app = Flask(__name__)
CORS(app)


@app.route("/api/send-key", methods=["POST"])
def get_key():
    global key
    data = request.json
    key = data.get("message")
    print(f"Key received: {key}")
    return ""


@app.route("/api/send-message", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message")
    print(f"Message received: {message}")
    print(f"Current key: {key}")
    return jsonify({"message": "Hello, World!"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=7359)
