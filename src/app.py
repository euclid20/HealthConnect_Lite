import os

from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
from src.config.setup import db


from src.config.setup import create_app
from src.routes.user_routes import user_blueprint
from src.routes.main_routes import main_blueprint
from src.routes.clinic_routes import clinic_blueprint
from src.models.clinic_model import Clinic


# Load environment variables from .env file
load_dotenv()

# Define flask application
app = create_app(os.getenv("CONFIG_MODE"))

# Register main_blueprint
app.register_blueprint(main_blueprint)

#Register clinic_blueprint
app.register_blueprint(clinic_blueprint)

# Register user_blueprint
app.register_blueprint(user_blueprint)

# Define route for creating the users table
@app.route("/")
def create_users_table():
    base_url = os.getenv('BASE_URL')
    return f"Server running on {base_url}:5000"



# Run only if the app.py is triggered direcly ( or app.py as the entry point of application )
if __name__ == "__main__":
    app.run(debug=True)
