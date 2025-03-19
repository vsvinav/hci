from openai import OpenAI
import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key="sk-bf8bfb31ec794bfe9f640c201a37922e", base_url="https://api.deepseek.com")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def get_hello_world():
    """
    Function to generate a creative "Hello World" message using OpenAI's API.
    """
    try:
        response = client.chat.completions.create(model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a creative AI that generates interesting greetings."},
            {"role": "user", "content": "Generate a unique 'Hello World' message."}
        ])
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Ensure API key is set
    if not client.api_key:
        print("Error: Please set your OpenAI API key in the environment variable 'OPENAI_API_KEY'.")
    else:
        print("Generated 'Hello World' message:")
        print(get_hello_world())


#sk-bf8bfb31ec794bfe9f640c201a37922e