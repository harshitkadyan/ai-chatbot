from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS (VERY IMPORTANT for frontend connection)
CORS(app)

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simple response logic
    reply = "Bot: You said " + user_message

    return jsonify({"response": reply})


# Health check (optional but useful)
@app.route("/")
def home():
    return "Chatbot API is running 🚀"


# Run app (for local + Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)