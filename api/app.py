from flask import Flask, render_template, request
from utils.recipe_helper import fetch_recipes, generate_response
import os, json

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        diet = request.form['diet']
        cuisine = request.form['cuisine']
        skill = request.form['skill']

        recipes = fetch_recipes(ingredients, diet, cuisine, skill)
        ai_response = generate_response(recipes, skill)

        try:
            parsed = json.loads(ai_response)
            results = parsed.get("recipes", [])
        except:
            results = [{"recipe_title": "Error", "description": "AI response error"}]

    return render_template('index.html', results=results)

# Required for Vercel
def handler(request):
    return app(request.environ, start_response=lambda status, headers: None)
