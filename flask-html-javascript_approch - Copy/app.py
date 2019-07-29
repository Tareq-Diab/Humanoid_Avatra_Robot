
import time
from threading import Thread

from flask import Flask, Response, render_template, request

from camera import VideoCamera

app = Flask(__name__)
app1=Flask("test")
pid=70
@app.route('/')
def index():
    
    
    return render_template('index.html')#,variable =var


def gen(camera):

    while True:
        frame = camera.get_frame(pid)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app1.route('/video_feed')
def video_feed():

    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def app_run():
    app.run(host='0.0.0.0')
    print("app.run started")
t2=Thread(target=app_run)
def app_run1():
    app1.run(host='0.0.0.0',port=5001)
    print("app.run started")
t3=Thread(target=app_run1)

def mod_pid():
    global pid

    
    while True:
        pid=int(input())



t4=Thread(target=mod_pid)


if __name__ == '__main__':

        t3.start()
        

        t2.start()
        t4.start()
