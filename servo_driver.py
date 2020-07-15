import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time
import socket



motors={"hip_lr":0,"knee_r":1,"hip_ll":2,"knee_l":3,
        "hip_ur":4,"hip_ul":5,"r_l_shoulder":6,"r_elbow":7,"l_l_shoulder":8,"l_elbow":9,"r_u_shoulder":10,"l_u_shoulder":11}
servos=[40,38,36,32,26,24,22,18,16,12,37,35,33,31,29,23,11,13]
for servo in servos:
    GPIO.setup(servo,GPIO.OUT)




hip_lr=GPIO.PWM(servos[0],50)
hip_lr.start(0)
knee_r=GPIO.PWM(servos[1],50)
knee_r.start(0)
hip_ll=GPIO.PWM(servos[2],50)
hip_ll.start(0)
knee_l=GPIO.PWM(servos[3],50)
knee_l.start(0)
r_elbow=GPIO.PWM(servos[motors["r_elbow"]],50)
r_elbow.start(0)

r_l_shoulder=GPIO.PWM(servos[motors["r_l_shoulder"]],50)
r_l_shoulder.start(0)

r_u_shoulder=GPIO.PWM(servos[motors["r_u_shoulder"]],50)
r_u_shoulder.start(0)

l_u_shoulder=GPIO.PWM(servos[motors["l_u_shoulder"]],50)
l_u_shoulder.start(0)

l_l_shoulder=GPIO.PWM(servos[motors["l_l_shoulder"]],50)
l_l_shoulder.start(0)

l_elbow=GPIO.PWM(servos[motors["l_elbow"]],50)
l_elbow.start(0)

u_neck=GPIO.PWM(11,50)
u_neck.start(0)

l_neck=GPIO.PWM(13,50)
l_neck.start(0)
"""
r_l_shoulder=GPIO.PWM(servos[motors["r_l_shoulder"]],50)
r_l_shoulder.start(0)


hip_ul=GPIO.PWM(servos[0],50)

hip_ur=GPIO.PWM(servos[3],50)

hip_ul.start(50)

hip_ur.start(50)
"""
def motor_check():
    left_leg=[[90,90,0,80,150,20,0],[90,30,0,80,150,20,0],[90,90,0,80,150,20,0],[30,90,0,80,150,20,0]]
    right_leg=[[30,90,80,80,150,20,0],[30,90,80,10,150,20,0],[30,90,80,80,150,20,0],[30,90,0,80,150,20,0]]
    right_arm=[[30,90,0,80,150,180,0],[30,90,0,80,150,90,0],[30,90,0,80,50,90,0],[30,90,0,80,190,90,0],[30,90,0,80,150,90,0],[30,90,0,80,150,90,180],[30,90,0,80,150,90,70],[30,90,0,80,150,20,0]]
    
    for x in left_leg:
        #x=x.split(",")
        
        time.sleep(0.8)
        

        angle_40=((((80+float(x[0]))/180)*9)+2.5)
        hip_lr.ChangeDutyCycle(angle_40)
        
        angle_38=(((float(x[1])/180)*9)+2.5)
        knee_r.ChangeDutyCycle(angle_38)
        
        angle_36=((((80-float(x[2]))/180)*9)+2.5)
        hip_ll.ChangeDutyCycle(angle_36)
        
        angle_32=((((150-float(x[3]))/180)*9)+2.5)
        knee_l.ChangeDutyCycle(angle_32)
        
        angle_18=((((230-float(x[4]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
        
        
        angle_22=((((180-float(x[5]))/180)*9)+2.5)

        r_l_shoulder.ChangeDutyCycle(angle_22)
        
        angle_37=((((float(x[6]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
      

    for x in right_leg:
        #x=x.split(",")
        time.sleep(0.8)
        

        angle_40=((((80+float(x[0]))/180)*9)+2.5)
        hip_lr.ChangeDutyCycle(angle_40)
        
        angle_38=(((float(x[1])/180)*9)+2.5)
        knee_r.ChangeDutyCycle(angle_38)
        
        angle_36=((((80-float(x[2]))/180)*9)+2.5)
        hip_ll.ChangeDutyCycle(angle_36)
        
        angle_32=((((150-float(x[3]))/180)*9)+2.5)
        knee_l.ChangeDutyCycle(angle_32)
        
        angle_18=((((230-float(x[4]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
        
        
        angle_22=((((180-float(x[5]))/180)*9)+2.5)

        r_l_shoulder.ChangeDutyCycle(angle_22)
        
        angle_37=((((float(x[6]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
    
    for x in right_arm:
        #x=x.split(",")
        time.sleep(0.8)
        

        angle_40=((((80+float(x[0]))/180)*9)+2.5)
        hip_lr.ChangeDutyCycle(angle_40)
        
        angle_38=(((float(x[1])/180)*9)+2.5)
        knee_r.ChangeDutyCycle(angle_38)
        
        angle_36=((((80-float(x[2]))/180)*9)+2.5)
        hip_ll.ChangeDutyCycle(angle_36)
        
        angle_32=((((150-float(x[3]))/180)*9)+2.5)
        knee_l.ChangeDutyCycle(angle_32)
        
        angle_18=((((230-float(x[4]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
        
        
        angle_22=((((180-float(x[5]))/180)*9)+2.5)

        r_l_shoulder.ChangeDutyCycle(angle_22)
        
        angle_37=((((float(x[6]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
        
    for x in [[0,90,180],[60,90,180],[-60,90,180],[0,90,180],[0,90,0],[0,90,180],[0,20,180]]:
        time.sleep(0.8)

        angle_12=((((90-float(x[0]))/180)*9)+2.5)
        
        l_elbow.ChangeDutyCycle(angle_12)
                
        angle_16=((((float(x[1]))/180)*9)+2.5)
        l_l_shoulder.ChangeDutyCycle(angle_16)
        angle_35=((((float(x[2]))/180)*9)+2.5)
        l_u_shoulder.ChangeDutyCycle(angle_35)

def dap():
    neck=[[75,150],[75,70],[75,90],[140,120],[30,70]]
    arms=[[90,0,0,180,30,-10],[90,0,40,180,120,-10]]
    for x in neck:
        time.sleep(0.3)
            
        angle_11=((((float(x[0]))/180)*9)+2.5)
        u_neck.ChangeDutyCycle(angle_11)
        
        angle_13=((((float(x[1]))/180)*9)+2.5)
        l_neck.ChangeDutyCycle(angle_13)
    
    for x in arms :
        
         
        angle_37=((((float(x[0]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
        
        angle_22=((((180-float(x[1]))/180)*9)+2.5)
        r_l_shoulder.ChangeDutyCycle(angle_22)
        
        angle_18=((((80-float(x[2]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
        

        angle_35=((((float(x[3]))/180)*9)+2.5)
        l_u_shoulder.ChangeDutyCycle(angle_35)

        
        angle_16=((((float(x[4]))/180)*9)+2.5)
        l_l_shoulder.ChangeDutyCycle(angle_16)
        
        angle_12=((((80-float(x[5]))/180)*9)+2.5)
        l_elbow.ChangeDutyCycle(angle_12)
        time.sleep(0.4)
    time.sleep(0.9)

        
    x=[10,30,0,180,30,-10]
             
    angle_37=((((float(x[0]))/180)*9)+2.5)
    r_u_shoulder.ChangeDutyCycle(angle_37)
        
    angle_22=((((180-float(x[1]))/180)*9)+2.5)
    r_l_shoulder.ChangeDutyCycle(angle_22)
        
    angle_18=((((80-float(x[2]))/180)*9)+2.5)
    r_elbow.ChangeDutyCycle(angle_18)
        

    angle_35=((((float(x[3]))/180)*9)+2.5)
    l_u_shoulder.ChangeDutyCycle(angle_35)

        
    angle_16=((((float(x[4]))/180)*9)+2.5)
    l_l_shoulder.ChangeDutyCycle(angle_16)
        
    angle_12=((((80-float(x[5]))/180)*9)+2.5)
    l_elbow.ChangeDutyCycle(angle_12)
    angle_11=((((float(75))/180)*9)+2.5)
    u_neck.ChangeDutyCycle(angle_11)
        
    angle_13=((((float(90))/180)*9)+2.5)
    l_neck.ChangeDutyCycle(angle_13)
time.sleep(1.5)
#dap()

motor_check()
print("ready to connect")
#------------------------------------

serversocket =socket.socket (socket.AF_INET,socket.SOCK_STREAM )
host   ="192.168.43.220"
print(host)
port=667
serversocket.bind((host,port))
serversocket.listen(3)

print("server intialized@"+str(host))
clientsocket ,adress=serversocket.accept()
print("recieve conection from:"+str(adress))

#------------------------------------
while True:
    try:
        
        #x=input() #for debuging (manual angel entery)
        x=(clientsocket.recv(2048)).decode('utf-8')
        if x=="off":
            break
        x=x.split(",")
        print(x)
        #print(x)
        
        
        
        angle_40=((((80+float(x[0]))/180)*9)+2.5)
        hip_lr.ChangeDutyCycle(angle_40)
                
        angle_38=(((float(x[1])/180)*9)+2.5)
        knee_r.ChangeDutyCycle(angle_38)
                
        angle_36=((((80-float(x[2]))/180)*9)+2.5)
        hip_ll.ChangeDutyCycle(angle_36)
                
        angle_32=((((150-float(x[3]))/180)*9)+2.5)
        knee_l.ChangeDutyCycle(angle_32)
                
                
        angle_37=((((float(x[8]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
                
        angle_18=((((80-float(x[4]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
                

                
        angle_35=((((float(x[9]))/180)*9)+2.5)
        l_u_shoulder.ChangeDutyCycle(angle_35)
                
                
                
        angle_22=((((180-float(x[5]))/180)*9)+2.5)

        r_l_shoulder.ChangeDutyCycle(angle_22)
                

                
        angle_12=((((80-float(x[7]))/180)*9)+2.5)
                
        l_elbow.ChangeDutyCycle(angle_12)
                        
        angle_16=((((float(x[6]))/180)*9)+2.5)
        l_l_shoulder.ChangeDutyCycle(angle_16)
                
 

        #-------------------------------------
        """
         
        angle_37=((((float(x[0]))/180)*9)+2.5)
        r_u_shoulder.ChangeDutyCycle(angle_37)
        
        angle_22=((((180-float(x[1]))/180)*9)+2.5)
        r_l_shoulder.ChangeDutyCycle(angle_22)
        
        angle_18=((((80-float(x[2]))/180)*9)+2.5)
        r_elbow.ChangeDutyCycle(angle_18)
        

        angle_35=((((float(x[3]))/180)*9)+2.5)
        l_u_shoulder.ChangeDutyCycle(angle_35)

        
        angle_16=((((float(x[4]))/180)*9)+2.5)
        l_l_shoulder.ChangeDutyCycle(angle_16)
        
        angle_12=((((80-float(x[5]))/180)*9)+2.5)
        l_elbow.ChangeDutyCycle(angle_12)

        """

     

        
        
    except:
        pass
clientsocket.close()
print("terminated")
