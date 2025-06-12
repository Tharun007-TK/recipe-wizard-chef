
# 🧙‍♂️ Recipe Wizard Chef

A fun and intelligent AI-powered recipe recommender that fuses the wisdom of a sweet grandma with the sass of Gordon Ramsay. Just toss in your ingredients and preferences—let the magic begin in the kitchen!

---

## 🍽️ Features

- 🧺 Ingredient-based recipe suggestions  
- 🧠 AI-generated instructions and commentary (via **Groq API**)  
- 🍅 Spoonacular API integration for real recipes  
- 🥦 Support for dietary restrictions, cuisine preferences, and cooking skill level  
- 🤖 Responses with flavor tips, warnings, and hilarious personality  

---

## 🔧 Tech Stack

- **Backend**: Python + Flask  
- **APIs**: Groq (LLM), Spoonacular (recipes)  
- **Frontend**: HTML, CSS (Jinja2 templates)  
- **Deployment**: Ready for Vercel (via Serverless functions)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/recipe-wizard-chef.git
cd recipe-wizard-chef
```

### 2. Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
SPOONACULAR_API_KEY=your_spoonacular_api_key
```

### 3. Install Dependencies

Make sure Python 3.10+ is installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Run Locally

```bash
python app.py
```

App will run on: [http://localhost:5000](http://localhost:5000)

---

## 💬 Example Prompt

**Input:**

- Ingredients: eggs, spinach, cheese  
- Diet: vegetarian  
- Cuisine: Italian  
- Skill: Beginner

**Output (AI):**
> "Oh sweetheart, let’s turn that fridge rubble into gold! Here's a classic Spinach Frittata...  
> And if you burn it, don’t cry—just add more cheese. Even Gordon agrees!"

---

## 🧠 Personality Mode

This app responds in "Grandma-Ramsay" mode:
- ❤️ Grandma's warmth  
- 🔥 Gordon's fire  
- 💡 Smart, funny, and personalized advice

---

## 🌐 Hosting on Vercel (Optional)

To deploy using Vercel:
1. Install [Vercel CLI](https://vercel.com/docs/cli)
2. Create a `vercel.json` file for serverless config
3. Deploy:

```bash
vercel deploy
```

Make sure environment variables are added in Vercel Dashboard.

---

## 📁 Project Structure

```
recipe-wizard-chef/
├── app.py
├── utils/
│   └── recipe_helper.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env
├── requirements.txt
└── README.md
```

---

## 📜 License

MIT License. Feel free to fork, remix, and cook up something awesome!

---

## ✨ Contributions

Pull requests and forks are welcome! If you’ve got improvements, bring them on, chef! 🍳
