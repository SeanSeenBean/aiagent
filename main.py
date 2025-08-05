import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

def main():
    if len(sys.argv) >= 2:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages)
    else:
        raise Exception("Invalid Input, program requires a single argument")
        sys.exit(1)
    if "--verbose" in sys.argv:
        print(
            f"User prompt: {user_prompt} \n"
            f"Prompt tokens: {response.usage_metadata.prompt_token_count} \n"
            f"Response tokens: {response.usage_metadata.candidates_token_count} \n"
        )

    print(response.text)


if __name__ == "__main__":
    main()
