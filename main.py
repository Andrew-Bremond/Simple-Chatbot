import openai
import asyncio
from openai import OpenAI

# openai.api_key = "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"

async def get_response(prompt):
    client = openai.AsyncOpenAI(api_key=openai.api_key)
    stream = await client.chat.completions.create(
        model="gpt-3.5-turbo",  # Updated model name
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    response = ""
    async for chunk in stream:
        if 'choices' in chunk and chunk.choices[0].delta.get('content'):
            response += chunk.choices[0].delta.content
    return response

async def main():
    print("Welcome to your Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = await get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    asyncio.run(main())