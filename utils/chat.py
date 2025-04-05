from google import genai
from dotenv import load_dotenv
import os
import json

#load environmental virables
load_dotenv()

def load_faq_context(json_file_path  = "faq_context.json"):
    with open(json_file_path, "r") as file:
        faq_list = json.load(file)

        #Convert to readable string for the prompt 

        faq_context = "\n".join(
            [f"Q: {item['question']} \nA: {item['answer']}" for item in faq_list]
        )
        return faq_context
    
#Base context for Alixia identity(INFORMATION)
BASE_CONTEXT = """
You are Alixia AI, an intelligent assistant for the Aliconnect platform.

Responsibilities:
- Help users with vendor support, product listings, marketing, customer care, logistics, etc.
- Be clear, helpful, and human-friendly.
- If unsure, suggest contacting human support.

Below is useful information you can use to answer user questions:
"""
# Chat Function for alixia
def user_chat(userPrompt= '') -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    #load faq context to merge it with base

    faq_context = load_faq_context()
    full_prompt = f"{BASE_CONTEXT}\n\nUser: {userPrompt}\nAlixia:"

    #Pass full user prompt to gemini ai
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[{"parts": [{"text": full_prompt}]}]
    )
    return response.text


print(user_chat("What is aliconnect all about?"))

#userInput = input("Enter your message: ")

#chat(userInput)
