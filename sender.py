"""*args
Application d'envoi de messages sur un broker RabbitMQ pour le cours d'OpenSource
Author: Jean-Hubert ABA'A
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.37'))
channel = connection.channel()

#Avant d'envoyer un message, on se rassure que la file des messages existe bien
channel.queue_declare(queue='ISIB')
#Et voilà nous pouvons envoyer un message
channel.basic_publish(exchange='', routing_key='ISIB', body='Vive l\'ISIB!!!!')

print("[x] sent a message")
connection.close()