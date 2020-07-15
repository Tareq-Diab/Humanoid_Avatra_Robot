import socket
import pygame
from pygame.locals import *
from threading import Thread
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time


servos=[40,38,36,32,26,37]
for servo in servos:
    GPIO.setup(servo,GPIO.OUT)



m5=GPIO.PWM(servos[13],50)


m5.start(0)


#--------------------------------------------------------
serversocket =socket.socket (socket.AF_INET,socket.SOCK_STREAM )
host   ="192.168.43.220"
print(host)
port=777
serversocket.bind((host,port))
serversocket.listen(3)

print("server intialized@"+str(host))

clientsocket ,adress=serversocket.accept()
print("recieve conection from:"+str(adress))
message='Thank you for connecting to the server'+'\r\n'
clientsocket.send(message.encode('utf-8'))
lastx=0
while True:
    try:
        

        message=clientsocket.recv(10)

        #print(str(message.decode('utf-8'))+"\n")
        x=(float(message.decode('utf-8')[:5])/180)*10
        print(round(x,1))
        if x>0 and ((last_x-x>0.1) or (last_x-x<-0.1)):

            m5.ChangeDutyCycle(round((11-x),1))
        last_x=x
        
    except:
        pass




