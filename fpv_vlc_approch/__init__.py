
from flask import Flask, render_template, Response,request
from camera import VideoCamera
from threading import Thread
import time

app = Flask(__name__)
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():

    return Response(gen(VideoCamera()),mimetype='image/svg; boundary=frame')
                    #mimetype='multipart/x-mixed-replace; boundary=frame')

def app_run1():
    app.run(host='0.0.0.0',port=5001)
    print("app.run started")
t3=Thread(target=app_run1)



if __name__ == '__main__':
    

        #t1.start()
        t3.start()
        

        #t2.start()


        

        
        

        

        
    
    
    
    

