from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import fitz  # PyMuPDF
import textwrap
from openai import OpenAI


app = Flask(__name__)
CORS(app)

global key
key = ""


@app.route("/api/send-key", methods=["POST"])
def get_key():
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
    try:
        response = client.Completion.create(
            engine="text-davinci-003", prompt=message, max_tokens=150
        )
        return jsonify({"message": response.choices[0].text.strip()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=7359)
