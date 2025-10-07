from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    question = input("\nAsk question: ")

    # Exit condition
    if question.lower() in ["exit", "quit", "bye", "close"]:
        print("Goodbye 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )

    print("\nAssistant:", response.choices[0].message.content)
    print("-" * 50)