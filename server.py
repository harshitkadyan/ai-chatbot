from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = "Bot: You said " + user_message
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)