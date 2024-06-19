from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import fitz  # PyMuPDF
import textwrap
from openai import OpenAI


app = Flask(__name__)
CORS(app)

key = ""


@app.route("/api/send-key", methods=["POST"])
def get_key():
    global key  # Declare key as global to modify the global variable
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
    client = OpenAI(api_key=key)
    return jsonify({"message": "Testing testing"})


if __name__ == "__main__":
    print(f"Initial key: {key}")
    app.run(debug=True, port=7359)
