from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat_app.html')

@app.route('/display_users')
def display_users():
    return render_template('display_users.html')

@socketio.on('message')
def handle_message(msg):
    print('メッセージ:', msg)

    # メッセージを接続されているすべてのクライアントに送信
    socketio.emit('message', msg)

@socketio.on('typing')
def handle_typing(data):
    print(f"{data['username']} is typing...")

    # タイピング中メッセージを接続されているすべてのクライアントに送信
    socketio.emit('typing', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)