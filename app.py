import os

from dotenv import load_dotenv
from flask import Flask

from routes.user_routes import user_blueprint

load_dotenv() # Load environment variables from .env file


app = Flask(__name__)

@app.route("/")
def __init__():
    base_url = os.getenv('BASE_URL');
    return f"Server running on {base_url}:5000"

app.register_blueprint(user_blueprint) # Register Routes

if __name__ == "__main__":
    app.run(debug=True)
