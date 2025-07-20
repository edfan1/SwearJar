from app import create_app, db, socketio

app = create_app()

# Replace @app.before_first_request with app context
with app.app_context():
    db.create_all()
    print("Database tables created!")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)