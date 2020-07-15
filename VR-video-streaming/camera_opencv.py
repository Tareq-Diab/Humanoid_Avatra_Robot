import cv2
from base_camera import BaseCamera
import numpy as np

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            i=70
            left=img[:,0:640-i]
            righ=img[:,0+i:640]
            numpy_horizontal_concat = np.concatenate((left, righ), axis=1)

            # encode as a jpeg image and return it
            
    
        
       

            #ret, jpeg = cv2.imencode('.jpg', numpy_horizontal_concat)
        
            #return jpeg.tobytes()

            yield cv2.imencode('.jpg', numpy_horizontal_concat)[1].tobytes()
