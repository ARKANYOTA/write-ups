# pip install "python-socketio[client]" requests websocket-client
import socketio
import json
import time

sio = socketio.Client()

@sio.event
def connect():
	sio.emit("message", "game_start")
	print('Connect')
	pass


i = 0
@sio.event
def message(msg_type, data):
	global i
	print('I received a message!', data)
	time.sleep(1)
	sio.send(["message", "wave_completed", json.dumps({"playerY": 200, "waveIndex": i})])
	i+=1


@sio.event
def disconnect():
	pass

# to send a message:
# sio.emit("message", "game_start")

sio.connect('https://space-traveler.404ctf.fr')
sio.wait()
