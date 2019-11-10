import base64
import cv2
import zmq
import sys
import argparse
import multiprocessing as mp

#########################################################################################################################
# https://stackoverflow.com/questions/4290834/how-to-get-a-list-of-video-capture-devices-web-cameras-on-linux-ubuntu-c
# You can use the following bash command:
# v4l2-ctl --list-devices
#In order to use the above command, you must install package v4l-utils before. In Ubuntu/Debian you can use the command:
# sudo apt-get install v4l-utils

def get_parser():
    parser = argparse.ArgumentParser(description="Detectron2 Demo")
    parser.add_argument("--ip", help="ip address to stream to")
    parser.add_argument(
        "--time",
        type=int,
        default=30,
        help="default amount of time to stream for",
    )
    return parser

args = get_parser().parse_args()
ip = args.ip
count = args.time
print(count)
counter = 0
context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://' + ip + ':5555')
camera = cv2.VideoCapture(0)  # init the first camera

while counter != count:
    print("camera 1")
    try:
        grabbed, frame = camera.read()  # grab the current frame
       # frame = cv2.resize(frame, (640, 480))  # resize the frame
        frame = cv2.resize(frame, (800,620))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
    
    counter+=1
    print(counter)

camera.release()
counter = 0
camera2 = cv2.VideoCapture(2)  # init the second camera

while counter != count:
    print("camera 2")
    try:
        grabbed, frame2 = camera2.read()  # grab the current frame
       # frame = cv2.resize(frame, (640, 480))  # resize the frame
        frame2 = cv2.resize(frame2, (800,620))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame2)
        jpg_as_text2 = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text2)

    except KeyboardInterrupt:
        camera2.release()
        cv2.destroyAllWindows()
        break
        
    counter+=1

camera2.release()
counter = 0
camera3 = cv2.VideoCapture(6)  # init the third camera

while counter != count:
    print("camera 3")
    try:
        grabbed, frame3 = camera3.read()  # grab the current frame
       # frame = cv2.resize(frame, (640, 480))  # resize the frame
        frame3 = cv2.resize(frame3, (800,620))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame3)
        jpg_as_text3 = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text3)

    except KeyboardInterrupt:
        camera3.release()
        cv2.destroyAllWindows()
        break
        
    counter+=1

camera3.release()
counter = 0
camera4 = cv2.VideoCapture(4)  # init the second camera

while counter != count:
    print("camera 4")
    try:
        grabbed, frame4 = camera4.read()  # grab the current frame
       # frame = cv2.resize(frame, (640, 480))  # resize the frame
        frame4 = cv2.resize(frame4, (800,620))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame4)
        jpg_as_text4 = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text4)

    except KeyboardInterrupt:
        camera4.release()
        cv2.destroyAllWindows()
        break
        
    counter+=1

camera4.release()
counter = 0
