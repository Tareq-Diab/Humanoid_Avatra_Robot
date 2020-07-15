import socket
import pygame
from pygame.locals import *
from threading import Thread
import time

def init_pygame():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pygame Keyboard Test')
    pygame.mouse.set_visible(1)

serversocket =socket.socket (socket.AF_INET,socket.SOCK_STREAM )
host   ="192.168.1.3"
port=666


#serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host,port))
serversocket.listen(3)
print("server intialized@"+str(host))
def com2():
    clientsocket ,adress=serversocket.accept()
    print("recieve conection from:"+str(adress))
    message='Thank you for connecting to the server'+'\r\n'
    clientsocket.send(message.encode('utf-8'))
    while True:
        message=clientsocket.recv(1024)

        print(str(message.decode('utf-8'))+"\n")



def com():
    while True:
        clientsocket ,adress=serversocket.accept()
        print("recieve conection from:"+str(adress))
        message='Thank you for connecting to the server'+'\r\n'
        clientsocket.send(message.encode('utf-8'))
        init_pygame()
        while True:

            events = pygame.event.get()
            
            for event in events:
                
                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_LEFT:
                        
                        message='left'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))
                        continue
                    

                        
                    if event.key == pygame.K_RIGHT:
                        message='right'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))
                                            
                    if event.key == pygame.K_UP:
                        message='up'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))
                        
                    if event.key == pygame.K_DOWN:
                        message='down'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))

                    if event.key == pygame.K_w:
                        message='w'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))

                    if event.key == pygame.K_s:
                        message='s'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))

                    if event.key == pygame.K_d:
                        message='d'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))
    
                    if event.key == pygame.K_a:
                        message='a'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))


                    if event.key == pygame.K_m: #motor checking
                        message='m'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))

                    if event.key == pygame.K_r: #shoulders reseting
                        message='r'
                        print(message)
                        clientsocket.send(message.encode('utf-8'))


                if event.type == pygame.KEYUP:
                    message='key-up'
                    print(message)
                    clientsocket.send(message.encode('utf-8'))
                    

                    

t1=Thread(target=com2)
t1.start()



