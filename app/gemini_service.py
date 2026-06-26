import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_prompt(user_input, platform, style):

    instruction = f"""
    User wants optimized prompts.

    Platform: {platform}
    Style: {style}

    User Query:
    {user_input}

    Generate:
    1. Category
    2. Optimized Prompt
    3. Three improvement tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=instruction
    )

    return response.text