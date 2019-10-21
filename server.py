from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

sensors = ['sensor1', 'sensor2', 'sensor3']

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/sensors', methods = ['GET'])
def list():
    return str(sensors)

@app.route('/api/sensors/<path:sensor_id>', methods = ['GET'])
def read(sensor_id):
    global sensors
    return sensors[sensor_id]

@app.route('/api/sensors', methods = ['POST'])
def create():
    sensors.append(request.json["sensorName"])
    return 'Added sensor!'


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    emit('json', json, broadcast=True)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/gauge')
def gauge():
    return render_template('gauge.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
