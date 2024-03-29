from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messagereceived():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('response', json, callback=messagereceived)


if __name__ == '__main__':
    socketio.run(app, debug=False)
