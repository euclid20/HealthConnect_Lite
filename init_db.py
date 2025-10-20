from src.app import app
from src.config.setup import db
from src.models.clinic_model import Clinic

with app.app_context():
    db.create_all()
    clinic1 = Clinic(name="Nairobi Wellness Center", location="Nairobi", contact="0712345678")
    clinic2 = Clinic(name="Mombasa Health Hub", location="Mombasa", contact="0723456789")

    db.session.add_all([clinic1, clinic2])
    db.session.commit()

    print("Database and sample clinics added.")