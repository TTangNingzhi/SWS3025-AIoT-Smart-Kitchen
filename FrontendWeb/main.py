import time
import paho.mqtt.client as mqtt
from joblib import load
import mqtt_back
from mqtt_back import on_connect, on_message, send_command, predict, info, client
from flask import Flask
from flask import request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'qwerty1234567890'

@app.route('/', methods=['GET'])
def index():
	client.loop_start()
	return render_template('index.html', t = info[0], p = info[1], h = info[2], s = info[3], f = info[4], a = info[5])

@app.route('/ledon', methods=['GET'])
def ledon():
	send_command('ledon')
	return redirect(url_for('index'))

@app.route('/ledoff', methods=['GET'])
def ledoff():
	send_command('ledoff')
	return redirect(url_for('index'))

@app.route('/bzon', methods=['GET'])
def bzon():
	send_command('bzon')
	return redirect(url_for('index'))

@app.route('/bzoff', methods=['GET'])
def bzoff():
	send_command('bzoff')
	return redirect(url_for('index'))

@app.route('/fanon', methods=['GET'])
def fanon():
	send_command('fanon')
	return redirect(url_for('index'))

@app.route('/fanoff', methods=['GET'])
def fanoff():
	send_command('fanoff')
	return redirect(url_for('index'))

@app.route('/pumpon', methods=['GET'])
def pumpon():
	send_command('pumpon')
	return redirect(url_for('index'))

@app.route('/pumpoff', methods=['GET'])
def pumpoff():
	send_command('pumpoff')
	return redirect(url_for('index'))

@app.route('/get', methods=['GET'])
def get():
	send_command('get')
	return redirect(url_for('index'))

@app.route('/detect', methods=['GET'])
def detect():
	send_command('detect')
	return redirect(url_for('index'))

@app.route('/end', methods=['GET'])
def end():
	send_command('end')
	return redirect(url_for('index'))
