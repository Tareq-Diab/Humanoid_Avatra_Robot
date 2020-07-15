
import argparse
import logging
import time

import common
import cv2


from estimator import TfPoseEstimator
from networks import get_graph_path, model_wh

from lifting.prob_model import Prob3dPose
from lifting.draw import plot_pose

import numpy as np
from threading import Thread
from npplot import *
#------------------------------------------------``

import socket

clientsocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host ="192.168.43.220"


port=667
clientsocket.connect((host,port))
clientsocket.send("master pc says hi\n".encode('utf-8'))

#--------------------------------------------------
#--------------------------video recording------------------------


#------------------------------------------------------------------

print("intiated1")


global pose_3d
pose_3d=[[
      [  12.82940148, -100.30240881,  -70.33411549 , -47.88706816 , 110.3646784,
     48.91913072 ,  59.16321995 ,  34.49412725 ,   4.28411421 , -46.74678603,
     -6.64194842 , 145.38996323 , 182.89336095 , 192.82483483 , -98.40667486,
   -161.45959738 ,-252.80748916],
   [  15.84084216 , 110.35759376   ,42.04545833  , 94.35015712  ,-78.67589366
  , -141.17304027 , -78.40770241  , 38.45974914  , 14.86075975 , -52.56037457
    ,-17.41718882 , -74.59002275 ,-152.16434207 ,-229.41350331 , 122.70442207,
    227.80423991 , 157.79090981],
  [ -61.98052206  ,-49.34881459 ,-463.7183776  ,-879.84092204  ,-23.44218217
   ,-462.13092401 ,-879.08603031 , 196.70130871 , 490.59708566 , 549.9238213
    ,700.9287918  , 466.23076523 , 206.04579191  , -2.33349679 , 465.88806215
    ,203.59293852  ,-41.8707693 ]]]
pose_3d=np.array(pose_3d)

#logger = logging.get#logger('TfPoseEstimator-WebCam')
#logger.setLevel(logging.DEBUG)
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
#formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
#ch.setFormatter(formatter)
#logger.addHandler(ch)


global humans
global image 
BREAK =False
def pose_dd():
    fps_time = 0
    global humans
    global BREAK 
    global image 
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)
    parser.add_argument('--zoom', type=float, default=1.0)
    parser.add_argument('--model', type=str, default='mobilenet_thin_432x368', help='cmu_640x480 / cmu_640x360 / mobilenet_thin_432x368')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    ##logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.model)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    #logger.debug('cam read+')
    cam = cv2.VideoCapture(args.camera)
    ret_val, image = cam.read()
    ##logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    while True:
        ret_val, image = cam.read()

        #logger.debug('image preprocess+')
        if args.zoom < 1.0:
            canvas = np.zeros_like(image)
            img_scaled = cv2.resize(image, None, fx=args.zoom, fy=args.zoom, interpolation=cv2.INTER_LINEAR)
            dx = (canvas.shape[1] - img_scaled.shape[1]) // 2
            dy = (canvas.shape[0] - img_scaled.shape[0]) // 2
            canvas[dy:dy + img_scaled.shape[0], dx:dx + img_scaled.shape[1]] = img_scaled
            image = canvas
        elif args.zoom > 1.0:
            img_scaled = cv2.resize(image, None, fx=args.zoom, fy=args.zoom, interpolation=cv2.INTER_LINEAR)
            dx = (img_scaled.shape[1] - image.shape[1]) // 2
            dy = (img_scaled.shape[0] - image.shape[0]) // 2
            image = img_scaled[dy:image.shape[0], dx:image.shape[1]]

        #logger.debug('image process+')
        humans = e.inference(image)

        #logger.debug('postprocess+')
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        #logger.debug('show+')
        cv2.putText(image,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()
        #out.write(image)
        if cv2.waitKey(1) == 27:
            #out.release()
            cv2.destroyAllWindows()
            BREAK = True
            clientsocket.send("off".encode('utf-8'))
            print("off sent")
            import sys
            sys.exit(0)
            break
        #logger.debug('finished+')
        #logger.info('3d lifting initialization.')
r_knee=joint(1,pose_3d[0])
r_hip=joint(0,pose_3d[0])
l_knee=joint(3,pose_3d[0])
l_hip=joint(2,pose_3d[0])
l_elbow=joint(7,pose_3d[0])
r_elbow=joint(5,pose_3d[0])
l_shoulder=joint(6,pose_3d[0])
r_shoulder=joint(4,pose_3d[0])
u_r_shoulder=joint("upper_right",pose_3d[0])
u_l_shoulder=joint("upper_left",pose_3d[0])


def pose_ddd():
    global pose_3d
    u_r_s=20
    u_l_s=180
    left_elbow_dir=1
    right_elbow_dir=1
    
    
    while True:
        try:
            poseLifting = Prob3dPose('./src/lifting/models/prob_model_params.mat')

            #image_h, image_w = image.shape[:2]
            standard_w = 640
            standard_h = 480

            pose_2d_mpiis = []
            visibilities = []
            for human in humans:
                pose_2d_mpii, visibility = common.MPIIPart.from_coco(human)
                pose_2d_mpiis.append([(int(x * standard_w + 0.5), int(y * standard_h + 0.5)) for x, y in pose_2d_mpii])
                visibilities.append(visibility)
            pose_2d_mpiis = np.array(pose_2d_mpiis)
            visibilities = np.array(visibilities)
            transformed_pose2d, weights = poseLifting.transform_joints(pose_2d_mpiis, visibilities)
            pose_3d = poseLifting.compute_3d(transformed_pose2d, weights)
            l_knee.update(pose_3d[0])
            l_hip.update(pose_3d[0])
            r_knee.update(pose_3d[0])
            r_hip.update(pose_3d[0])
            l_elbow.update(pose_3d[0])
            r_elbow.update(pose_3d[0])
            l_shoulder.update(pose_3d[0])
            r_shoulder.update(pose_3d[0])
            u_r_shoulder.update(pose_3d[0])
            u_l_shoulder.update(pose_3d[0])


            
            if u_r_shoulder.joint_angle < 30 :
                u_r_s=90
            elif  u_r_shoulder.joint_angle > 30 :
                u_r_s=20 # down
            
            if u_l_shoulder.joint_angle < 30 :
                u_l_s=90
            elif u_l_shoulder.joint_angle > 30:
                u_l_s=180 # down
            

            #right  15:elbow , right 16: hand 
            if pose_3d[0][0,15] > pose_3d[0][0,16]:
                right_elbow_dir=1
            elif  pose_3d[0][0,15] < pose_3d[0][0,16]:
                right_elbow_dir=-1
            

            if pose_3d[0][0,12] > pose_3d[0][0,13]:
                left_elbow_dir=1
            elif pose_3d[0][0,12] < pose_3d[0][0,13]:
                left_elbow_dir=-1
            
            message=str(r_hip.joint_angle)+','+str(r_knee.joint_angle-90)+','+str(l_hip.joint_angle)+','+str(l_knee.joint_angle-90)+','+str(right_elbow_dir*(r_elbow.joint_angle-140))+','+str(r_shoulder.joint_angle)+','+str(l_shoulder.joint_angle)+','+str(left_elbow_dir*(l_elbow.joint_angle-145))+','+str(u_r_s)+','+str(u_l_s)#","+str(l_knee.joint_angle-90)+','+str(r_hip.joint_angle)+","+str(r_knee.joint_angle-90)
            
            clientsocket.send(message.encode('utf-8'))

            
            if BREAK == True:
                clientsocket.send("off".encode('utf-8'))
                print("off sent")
                break

            

            
            
            
        except :
            pass

def angels_to_speach():
    import win32com.client as wincl
    while True :
        try:
            #"knee"+str(int(knee.joint_angle))
            speak = wincl.Dispatch("SAPI.SpVoice")
            #speak.Speak("knee"+str(int(knee.joint_angle)-90))
            #speak.Speak("elbow  is "+ str(int (l_elbow.joint_angle) ))
            #speak.Speak("special is "+ str(u_l_shoulder.special))
            #speak.Speak("the relation is ")
            
            if u_l_shoulder.joint_angle < 20 :
                speak.Speak("up")
            
            else :
                speak.Speak("down")
            
            """
            #right  15:elbow , right 16: hand 
            if pose_3d[0][0,15] > pose_3d[0][0,16]:
                speak.Speak("positive"+str(int (r_elbow.joint_angle-140)))
            elif  pose_3d[0][0,15] < pose_3d[0][0,16]:
                speak.Speak("negative"+str(int(r_elbow.joint_angle-140)))
            """
            """
            #  12:right elbow , right 13: hand 
            if pose_3d[0][0,12] > pose_3d[0][0,13]:
                speak.Speak("positive"+str(int (l_elbow.joint_angle)))
            elif pose_3d[0][0,12] < pose_3d[0][0,13]:
                speak.Speak("negative"+str(int(l_elbow.joint_angle)))
            """


            if BREAK == True :

                break

        except :
            pass



speak_thread=Thread(target=angels_to_speach)

dd_thread=Thread(target=pose_dd)
ddd_thread=Thread(target=pose_ddd)
if __name__ == '__main__':
    
    dd_thread.start()
    ddd_thread.start()
    #speak_thread.start()
    #ai=animation.FuncAnimation(fig, body_plotting,fargs=(pose_3d[0],), interval=1)
    #plt.show()
    
    

    











