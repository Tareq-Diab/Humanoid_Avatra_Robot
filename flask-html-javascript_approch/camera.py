import cv2

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 620)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 160);
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 120);
        


    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        
        gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()
VideoCamera()

