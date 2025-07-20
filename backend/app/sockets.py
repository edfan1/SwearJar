from app import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('contribution_added')
def handle_new_contribution(data):
    socketio.emit('jar_updated', data, broadcast=True)

