from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import pymupdf
import textwrap
from openai import OpenAI

API_KEY = ""

client = OpenAI(api_key=API_KEY)

app = Flask(__name__)
CORS(app)

key = ""

@app.route("/api/send-message", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message")
    print(message)
    return jsonify({"message": "Testing testing"})


@app.route("/api/send-key", methods=["POST"])
def get_key():
    data = request.json
    key = data.get("key")
    print(key)
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=7359)
