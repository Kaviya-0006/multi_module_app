from flask import Flask
import requests

app = Flask(__name__)

MODULE1_URL = "http://module1-service:5000"
MODULE2_URL = "http://module2-service:5001"

@app.route("/")
def home():
    # Call module1 and module2 independently
    users_page = requests.get(f"{MODULE1_URL}/users").text
    module2_index = requests.get(f"{MODULE2_URL}/").text

    combined = f"Module1 Users Preview:\n{users_page[:200]}...\n\nModule2 Index Preview:\n{module2_index[:200]}..."
    return f"<pre>{combined}</pre>"

if __name__ == "__main__":
    app.run(port=5002, debug=True)