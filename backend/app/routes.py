from flask import Blueprint, jsonify, request
from app.models import User, SwearJar, Contribution
from app import db

main = Blueprint('main', __name__)

@main.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@main.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username})

@main.route('/api/jars', methods=['GET'])
def get_jars():
    jars = SwearJar.query.all()
    return jsonify([{
        'id': jar.id, 
        'name': jar.name,
        'current_amount': jar.current_amount,
        'goal_amount': jar.goal_amount
    } for jar in jars])

@main.route('/api/jars', methods=['POST'])
def create_jar():
    data = request.json
    jar = SwearJar(
        name=data['name'],
        description=data.get('description', ''),
        goal_amount=data.get('goal_amount', 0.0),
        current_amount=data.get('current_amount', 0.0)
    )
    db.session.add(jar)
    db.session.commit()
    return jsonify({
        'id': jar.id,
        'name': jar.name,
        'description': jar.description,
        'goal_amount': jar.goal_amount,
        'current_amount': jar.current_amount
    })

@main.route('/api/contribute', methods=['POST'])
def add_contribution():
    data = request.json
    contribution = Contribution(
        user_id=data['user_id'],
        jar_id=data['jar_id'],
        amount=data['amount'],
        swear_word=data.get('swear_word', '')
    )
    db.session.add(contribution)
    
    # Update jar's current amount
    jar = SwearJar.query.get(data['jar_id'])
    jar.current_amount += data['amount']
    
    db.session.commit()
    return jsonify({'success': True})

@main.route('/api/test', methods=['GET'])
def test_endpoint():
    print("Test endpoint accessed!")
    return jsonify({
        'status': 'success',
        'message': 'Backend is up and running!'
    })