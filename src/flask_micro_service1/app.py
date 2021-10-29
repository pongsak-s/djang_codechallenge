from flask import Flask
from flask import jsonify
from time import sleep
from threading import Thread
from channel_wrapper import queue_listening

import random

app = Flask(__name__)

@app.route('/service2')
def service1():
	''' mock slow service from 5 to 15 seconds '''
	delay_time = random.randint(5, 15)
	sleep(delay_time)
	return jsonify(
        message="This is mocking slow service with random delay: "+str(delay_time)+" seconds.",
    )

if __name__ == "__main__":
	# start queue listening to service1 queue with threading
	thread = Thread(target = queue_listening)
	thread.start()
	# start flask as usual
	app.run(host='0.0.0.0', port=5000)

