import os

from dotenv import load_dotenv
from flask import Flask
from flask_mysqldb import MySQL

from routes.user_routes import user_blueprint

# Load environment variables from .env file
load_dotenv() 

# Define flask application
app = Flask(__name__)

# Define route for creating the users table
@app.route("/")
def create_users_table():
    base_url = os.getenv('BASE_URL')
    return f"Server running on {base_url}:5000"

# Register Routes
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
