from django.shortcuts import render
from django.http import HttpResponse
import pika
import json


class Service1():
    """Represent service1 that may need to take queue """

    def call(request):
        sms_queue = ServiceQueue("localhost")
        data = {
        	"phone": "+66-92-123-4567",
        	"message": "mocking message"
        }
        sms_queue.send(request, data)
        return HttpResponse(json.dumps({ "message" : "submit to queue successfully!" }))


class ServiceQueue():
    """Represent queue for interacting with flask """

    def __init__(self, host_url):
        self.host_url = host_url

    def send(self, request, data_obj):
        """Calling to RabbitMQ
        
        This simple function will interact with rabbitmq message queue.
        
        Args: 
            request - http request received from urls.py
            data_obj - data object to send to queue
        
        Returns:
            None
        """
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host_url))
        channel = connection.channel()
        channel.queue_declare(queue='sms_queue')
        channel.basic_publish(exchange='', routing_key='sms_queue', body=json.dumps(data_obj))
        print(" [x] Submit service task to queue'")
        connection.close()
        #return HttpResponse("test")

