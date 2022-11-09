import time
import paho.mqtt.client as mqtt
from joblib import load

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT Broker!")
	else:
		print('Failed to connect, return code {:d}'.format(rc))

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print('Received message: {}'.format(data))
    cmd = predict(data)
    if (cmd == 1):
        info[5] = 'Dangerous!'
        send_command('ledon')
        send_command('bzon')
        send_command('fanon')
        send_command('pumpon')
    elif (cmd == 2):
        info[5] = 'Uncomfortable!'
        send_command('ledon')
        send_command('bzoff')
        send_command('fanon')
        send_command('pumpoff')
    else:
        info[5] = 'Comfortable!'
        send_command('ledoff')
        send_command('bzoff')
        send_command('fanoff')
        send_command('pumpoff')
        
    print('Prediction result: ' + info[5])
            
def send_command(cmd):
    result = client.publish(topic_command, cmd)
    status = result[0]
    if status == 0:
        print('Send command {} successfully!'.format(cmd))
    else:
        print('Failed to send command to Raspberry Pi.')
        
def predict(data):
    buffer = data.split(';')
    for index in range(5):
        buffer[index] = float(buffer[index].split(':')[1])
        info[index] = buffer[index]
    cmd = rfc.predict(scl.transform([buffer]))[0]
    return cmd
    
try:
    info = [0, 0, 0, 0, 0, 'None']
    
    scl = load('scalar.joblib')
    rfc = load('rfc.joblib')
    
    broker = 'broker.emqx.io'
    port = 1883
    topic_command = '/sws3025/command'
    topic_message = '/sws3025/message'
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    
    client.subscribe(topic_message)
    client.on_message = on_message

except KeyboardInterrupt:
    print('Program terminated!')