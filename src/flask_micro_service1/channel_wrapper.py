import pika, sys, os, json

def start_queue_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sms_queue')

    def callback(ch, method, properties, body):
        print(" [x] MQ Received %r" % json.loads(body))

    channel.basic_consume(queue='sms_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for queue messages.')
    channel.start_consuming()

def queue_listening():

    try:
        start_queue_consuming()
    except:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


