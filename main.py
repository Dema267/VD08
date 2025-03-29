from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_quote():
    """Запрашивает случайную цитату с API Quotable."""
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return {
                "content": data["content"],
                "author": data["author"]
            }
        return {"content": "Failed to fetch quote.", "author": "System"}
    except:
        return {"content": "Error connecting to API.", "author": "System"}

def get_random_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        return {
            "content": data["q"],
            "author": data["a"]
        }
    except:
        return {"content": "Life is what happens when you're busy making other plans.", "author": "John Lennon"}



@app.route("/")
def home():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)