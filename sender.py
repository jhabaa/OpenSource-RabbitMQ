"""*args
Application d'envoi de messages sur un broker RabbitMQ pour le cours d'OpenSource
Author: Jean-Hubert ABA'A
"""

import pika
import tkinter
import asyncio
from tkinter import *
from tkinter import ttk

def SendMessage():
    messageVariable.set(messageZone.get())
    message = messageVariable.get()
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.37'))
    channel = connection.channel()
    #Avant d'envoyer un message, on se rassure que la file des messages existe bien
    channel.queue_declare(queue='ISIB')
    #Prendre le message au clavier
    #toSend = input("Entrer le message a envoyer")
    #Et voila nous pouvons envoyer un message
    channel.basic_publish(exchange='', routing_key='ISIB', body=message)
    print("[x] sent a message")
    connection.close()
    labelStatus.set("Message Envoyé")
    labelStatus.set("")


root = Tk()
root.geometry("200x400")
frame = Frame(root)
frame.pack()


messageVariable =StringVar()
messageZone = ttk.Entry(frame)
messageZone.insert(0, "Entrer Votre message Ici ...")
messageZone.pack()

sendBtn = Button(frame, text = "Send", command=SendMessage)
sendBtn.pack()

labelStatus = StringVar()
statusZone = Label(frame, textvariable=labelStatus)
statusZone.pack()

root.title("Sender RabbitMQ")
root.mainloop(0)

