import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 620)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 320);
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000);
        


    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        numpy_horizontal_concat = np.concatenate((image, image), axis=1)
        
       

        ret, jpeg = cv2.imencode('.jpg', numpy_horizontal_concat)
        
        return jpeg.tobytes()
VideoCamera()

