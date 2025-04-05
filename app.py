from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.chat import user_chat

app = Flask(__name__)

CORS(app)

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
    
""" 
    responses = {
        "how do i sign up": "You can sign up by visiting our website and clicking on the ‘Sign Up’ button.",
        "how do i create an account": "You can create an account by signing up on our website.",
        "how do i join": "You can join by registering on our platform through the signup page.",
    }

    bot_response = responses.get(user_message, "I'm not sure about that. Can you rephrase?")
    
    return jsonify({"response": bot_response}) """


if __name__ == "__main__":
    app.run(debug=True)
