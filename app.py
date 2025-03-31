from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Alixia AI is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  
    user_message = data.get("message", "").lower()  
    

    responses = {
        "how do i sign up": "You can sign up by visiting our website and clicking on the ‘Sign Up’ button.",
        "how do i create an account": "You can create an account by signing up on our website.",
        "how do i join": "You can join by registering on our platform through the signup page.",
    }

    bot_response = responses.get(user_message, "I'm not sure about that. Can you rephrase?")
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
