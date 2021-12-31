"""[summary]
    Application qui reçoit les messages du broker
    """

from asyncio.tasks import wait_for
from time import localtime, time
import pika
import tkinter
import asyncio
from tkinter import *
from tkinter import ttk
from datetime import datetime
import time

textreceived = "Messages Recus"
messageList = ""
textState = "Ecouter"
message = ""
#Souscription
def callback(ch,method, properties, body):
    global textreceived, messageList
    print("[x] Received %r " %body)
    #receivedMessage.set("Voile")
    t = localtime()
    dateAndtext = str(time.strftime("%H:%M:%S",t)) + " : " + str(body) 
    #receivedMessage.set(body)
    #messageList.insert(0,dateAndtext)
    messageList = str(messageList) + str(dateAndtext) + "\n"
    receivedMessage.set(messageList)
    root.update()

def accDelete(list):
    global message
    for a in range(list):
        message = message + a + "\n"
    


def Listen():
    global textState
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.37'))
    channel = connection.channel()
    #On commence par créer la file ou s'assure qu'elle existe
    channel.queue_declare(queue='ISIB')
    #Et on informe RabbitMQ que le callback recoit un message du Topic
    channel.basic_consume(queue='ISIB', auto_ack=True, on_message_callback=callback)
    #Enfin nous entrons dans une boucle sans fin pour toujour écouter sur le topic
    #receivedMessage.set( receivedMessage.get() + "[x] Waiting for messages \n")
    channel.start_consuming()
    textState = "En Ecoute..."
    root.update()
    


root = Tk()
root.geometry("200x400")
frame = Frame(root)
frame.pack()
labelStatus = StringVar()
labelStatus.set('Pour écouter, cliquer sur le bouton')
statusZone = Label(frame, textvariable=labelStatus)
statusZone.pack()

btnText = StringVar()
btnText.set(textState)
sendBtn = Button(frame, textvariable= btnText, command=Listen )
sendBtn.pack()
receivedMessage = StringVar()
receivedMessage.set(messageList)
receivedZone = Label(frame, textvariable=receivedMessage)
receivedZone.pack()
root.title("Sender RabbitMQ")
root.mainloop()

#root.update()


