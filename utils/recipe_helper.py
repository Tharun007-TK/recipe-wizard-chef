import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
spoonacular_key = os.getenv("SPOONACULAR_API_KEY")

def fetch_recipes(ingredients, diet, cuisine, skill_level):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "includeIngredients": ingredients,
        "diet": diet,
        "cuisine": cuisine,
        "number": 3,
        "apiKey": spoonacular_key
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

def generate_response(recipes, skill_level):
    recipe_names = ", ".join([r['title'] for r in recipes])
    prompt = f"""
You are a JSON API generator, acting like a friendly grandma with Gordon Ramsay sass.
The user is a {skill_level} level cook.

Given the following recipes: {recipe_names}, respond with only valid JSON in this format:

{{
  "recipes": [
    {{
      "recipe_title": "string",
      "description": "string",
      "tip": "string",
      "warning": "string",
      "funny_comment": "string"
    }}
  ]
}}

Do not include explanations, greetings, markdown, or any extra text.
Just return the JSON.
"""

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a JSON-only recipe assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    response.raise_for_status()
    content = response.json()['choices'][0]['message']['content'].strip()

    if content.startswith("```"):
        content = content.split("```")[1].strip()

    try:
        return json.loads(content)["recipes"]
    except json.JSONDecodeError as e:
        print("⚠️ JSON error:", e)
        return [{"recipe_title": "Parse Error", "description": "AI response invalid."}]
