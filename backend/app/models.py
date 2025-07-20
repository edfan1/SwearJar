from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contributions = db.relationship('Contribution', backref='contributor', lazy=True)

class SwearJar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Float)
    current_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    contributions = db.relationship('Contribution', backref='jar', lazy=True)

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    jar_id = db.Column(db.Integer, db.ForeignKey('swear_jar.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    swear_word = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)