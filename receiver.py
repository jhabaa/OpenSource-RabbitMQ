"""[summary]
    Application qui reçoit les messages du broker
    """

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.37'))
channel = connection.channel()
    
#On commence par créer la file ou s'assure qu'elle existe
channel.queue_declare(queue='ISIB')

#Souscription
def callback(ch,method, properties, body):
    print("[x] Received %r " %body)
    
#Et on informe RabbitMQ que le callback recoit un message du Topic
channel.basic_consume(queue='ISIB', auto_ack=True, on_message_callback=callback)

#Enfin nous entrons dans une boucle sans fin pour toujour écouter sur le topic
print("[x] Waiting for messages")
channel.start_consuming()