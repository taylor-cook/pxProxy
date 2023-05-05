import requests
from flask import Flask, render_template
from flask-socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# function to get data from JSONPlaceholder API
def get_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()

# socket.io event to emit data to the client
@socketio.on('connect')
def test_connect():
    data = get_data()
    emit('data', data)

if __name__ == '__main__':
    socketio.run(app)
