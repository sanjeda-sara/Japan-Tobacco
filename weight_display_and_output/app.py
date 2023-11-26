from flask import Flask, render_template
from flask_socketio import SocketIO, emit
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
 
# Initial values
raw_weight_value = 0
discount_value = 0
final_weight_value = 0
 
@app.route('/')
def index():
    return render_template('result.html')
 
@app.route('/text')
def text():
    raw_weight_value = 40
    discount_value = 2
    final_weight_value = raw_weight_value - discount_value
    # Emit updates for raw weight, discount, and final weight with different messages
    socketio.emit('updateRawWeight', {'data': raw_weight_value})
    socketio.emit('updateDiscount', {'data': discount_value})
    socketio.emit('updateFinalWeight', {'data': final_weight_value})
    return "Text updated!"
 
@socketio.on('connect')
def handle_connect():
    # Send the initial values to the newly connected client
    emit('updateRawWeight', {'data': raw_weight_value})
    emit('updateDiscount', {'data': discount_value})
    emit('updateFinalWeight', {'data': final_weight_value})
    return True
 
if __name__ == '__main__':
    socketio.run(app, debug=True)