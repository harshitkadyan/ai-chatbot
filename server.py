from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# Homepage (UI)
@app.route("/")
def home():
    return render_template_string("""
    <h2>AI Chatbot</h2>
    <input id="msg" placeholder="Type message">
    <button onclick="sendMsg()">Send</button>
    <p id="response"></p>

    <script>
    function sendMsg() {
        let msg = document.getElementById("msg").value;
        fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg})
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("response").innerText = data.response;
        });
    }
    </script>
    """)

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = "Bot: You said " + user_message
    return jsonify({"response": reply})

# Run properly for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)