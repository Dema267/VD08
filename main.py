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

@app.route("/")
def home():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)