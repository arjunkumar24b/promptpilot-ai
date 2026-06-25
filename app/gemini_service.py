from google import genai

# Paste your Gemini API key here
API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)


def generate_prompt(user_input, platform, style):

    instruction = f"""
You are PromptPilot AI.

Transform vague user queries into highly effective prompts.

User Query:
{user_input}

Target AI Platform:
{platform}

Desired Style:
{style}

Generate:
1. Category
2. Optimized Prompt
3. Three improvement tips.

Return the response in a clear format.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=instruction
    )

    return response.text