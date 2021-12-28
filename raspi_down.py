import serial
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print('Failed to connect, return code {:d}'.format(rc))

def on_message(client, userdata, msg):
    cmd = msg.payload.decode()
    print('Received command from cloud: {}'.format(cmd))
    print('Send command to Micro:bit: {}'.format(cmd))
    sendCommand(cmd)
    
    
def sendCommand(command):
    command = command + '\n'
    ser.write(str.encode(command))
    
try:
    
    broker = 'broker.emqx.io'
    port = 1883
    topic = '/sws3025/command'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    
    print('Listening on /dev/ttyACM0.')
    ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 115200, timeout = 1)

    client.subscribe(topic)
    client.on_message = on_message
#    client.loop_forever()

except KeyboardInterrupt:
    
    if ser.is_open:
        ser.close()
    print('Program terminated!')
