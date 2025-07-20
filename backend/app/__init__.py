from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    # Init CORS
    # For prod change to frontend url
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    
    from app.routes import main
    app.register_blueprint(main)
    print("Routes registered:", [rule.rule for rule in app.url_map.iter_rules()])
    
    return app