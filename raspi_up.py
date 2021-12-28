import serial
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print('Failed to connect, return code {:d}'.format(rc))

def waitResponse():
    response = ser.readline()
    response = response.decode('utf-8').strip()
    return response

try:
    
    broker = 'broker.emqx.io'
    port = 1883
    topic = '/sws3025/message'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    
    print('Listening on /dev/ttyACM0')
    ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 115200, timeout = 1)

    client.loop_start()
    while True:
        time.sleep(1)
        msg = waitResponse()
        if msg != "":
            print('Receive message from Micro:bit: {}'.format(msg))
            result = client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print('Send the message to cloud successfully!')
            else:
                print('Failed to send message to cloud.')

except KeyboardInterrupt:
    
    if ser.is_open:
        ser.close()
    print('Program terminated!')
    

