from google import genai
from dotenv import load_dotenv
import os
import json
from bs4 import BeautifulSoup
import requests
from product import load_products
#load environmental virables
load_dotenv()

def load_faq_context(json_file_path="faq_context.json"):
    try:
        with open(json_file_path, "r") as file:
            faq_list = json.load(file)
            faq_context = "\n".join(
                [f"Q: {item['question']} \nA: {item['answer']}" for item in faq_list]
            )
            return faq_context
    except Exception as e:
        return (f"Error loading FAQ context: {e}")
    
""" def load_products():
    aliconnects_store_url = os.getenv("ALICONNECT_STORE_URL")
    response = requests.get(aliconnects_store_url)
    soup = BeautifulSoup(response.text, "html.paser")
    tags = soup.findAll("img, h2, p, a", limit=100)
    for tag in tags:
        print(tag.text) """
   
#Base context for Alixia identity(INFORMATION)
BASE_CONTEXT = """
You are Alixia AI, an intelligent assistant for the Aliconnect platform.

Responsibilities:
- Help users with customer support, product inquiries, order status, and general platform navigation.
- You can also try to make your grammar more better also according to the context provided to you, also try to understand customers grammar and typo(S)
- Be clear, helpful, and human-friendly.
- Make sure you don't write or do coding for any customer, Instead, reply what your purpose is for.
- You'ree an Ai and you don't have feeling at all
- If unsure of any customer prompt, suggest them to contact human support Team at <a href='mailto:support@aliconnect.com' style='color: blue; text-decoration: underline;'>support@aliconnect.com</a>
- Lastly, If you got a right response for the user question (Concerning only question and not greetings), start your word with 'Got it', also give paragraph in your response or comma'(),'
- If user ask or type a product name, reply with the product image, price and more, you can scrape the product info from https://store.aliconnects.com/?product_cat=0&s={userSearch}&post_type=product , (The {userSearch should be the product the user asked for} Please reason) there should be a search for it, also return the response as good designed html elements with style attribute for reactjs (JSX)
"""

# Chat Function for alixia
def user_chat(userPrompt= '') -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    #load faq context to merge it with base

    faq_context = load_faq_context()
    full_prompt = f"{BASE_CONTEXT}\n{faq_context}\n\n {load_products(userPrompt)} User: {userPrompt}\nAlixia:"


    #Pass full user prompt to gemini ai
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[{"parts": [{"text": full_prompt}]}]
    )
    return response.text


#Testing the chat->
""" userInput = input("Enter your message: ")

print(user_chat(userInput))
 """