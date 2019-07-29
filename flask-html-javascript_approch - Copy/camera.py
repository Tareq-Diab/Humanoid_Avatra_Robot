import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 620)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);
        #self.image=cv2.imread("black.jpg")
        #self.image = cv2.resize(self.image, (30, 480)) 

        


    
    def __del__(self):
        self.video.release()


    
    def get_frame(self,pid):
        success, image = self.video.read()
        i=pid
        left=image[:,0:640-i]
        righ=image[:,0+i:640]
        numpy_horizontal_concat = np.concatenate((left, righ), axis=1)
        #numpy_horizontal_concat = np.concatenate((numpy_horizontal_concat, image), axis=1)
    
        
       

        ret, jpeg = cv2.imencode('.jpg', numpy_horizontal_concat)
        
        return jpeg.tobytes()
VideoCamera()

