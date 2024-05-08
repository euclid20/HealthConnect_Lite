import os

from dotenv import load_dotenv
from flask import Flask

from config.setup import create_app
from routes.user_routes import user_blueprint

# Load environment variables from .env file
load_dotenv()

# Define flask application
app = create_app(os.getenv("CONFIG_MODE"))

# Define route for creating the users table
@app.route("/")
def create_users_table():
    base_url = os.getenv('BASE_URL')
    return f"Server running on {base_url}:5000"

# Register Routes
app.register_blueprint(user_blueprint)

# Run only if the app.py is triggered direcly ( or app.py as the entry point of application )
if __name__ == "__main__":
    app.run(debug=True)
