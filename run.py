from src.app import app
from src.config.setup import create_app, db
from src.models.clinic_model import Clinic
from src.models.user_model import User
from src.routes.clinic_routes import clinic_blueprint
from src.routes.user_routes import user_blueprint

app = create_app()

app.register_blueprint(clinic_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
        if not Clinic.query.first():
            sample = Clinic(name="HealthCare Center", location="Nairobi", contact="0712345678")
            db.session.add(sample)
            db.session.commit()

    app.run(debug=True)
