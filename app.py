from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.chat import user_chat

app = Flask(__name__)

CORS(app, origins="https://aliconnect-chat-client.vercel.app")



@app.route("/")
def home():
    return "Alixia AI is up and running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  
    user_message = data.get("message", "").lower()  

    if not user_message:
        return jsonify({"error": "no message provided"}), 400
    
    try:
        ai_response = user_chat(user_message)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == "__main__":
    app.run(debug=True)
