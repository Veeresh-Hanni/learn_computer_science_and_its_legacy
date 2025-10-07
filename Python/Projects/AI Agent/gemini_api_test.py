import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
chat = genai.GenerativeModel("gemini-2.5-pro").start_chat()

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye👋.")
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)