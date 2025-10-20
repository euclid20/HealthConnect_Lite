from flask import Blueprint, jsonify, request
from src.config.setup import db
from src.models.clinic_model import Clinic

clinic_blueprint = Blueprint('clinic_bp', __name__)

#GET route- fetch all clinics
@clinic_blueprint.route('/clinics', methods=['GET'])
def get_clinics():
    clinics = Clinic.query.all()
    result = [
        {
            'id': clinic.id,
            'name': clinic.name,
            'location': clinic.location,
            'contact': clinic.contact
        }
        for clinic in clinics
    ]
    return jsonify(result)

#POST route - add a new clinic
@clinic_blueprint.route('/clinics', methods=['POST'])
def add_clinic():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    contact = data.get('contact')

    if not all([name, location, contact]):
        return jsonify({'error': 'Missing fields'}), 400
    
    if not contact.startswith('07') or len(contact) != 10 or not contact.isdigit():
        return jsonify({'error': 'Invalid contact format. Use Kenyan mobile format like 0712345678'}), 400


    new_clinic = Clinic(name=name, location=location, contact=contact)
    db.session.add(new_clinic)
    db.session.commit()

    return jsonify({'message': 'Clinic added successfully'}), 201
