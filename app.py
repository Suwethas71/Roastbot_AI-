from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Serve frontend
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"""
You are a savage, witty, sarcastic chatbot.
Roast playfully. No religion, caste, hate, or real people.

User: {user_msg}
""",
                "stream": False
            },
            timeout=60
        )

        reply = response.json()["response"]
        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "AI is buffering its brain 🧠"}), 500


if __name__ == "__main__":
    app.run(debug=True)
