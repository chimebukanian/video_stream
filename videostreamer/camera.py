import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.capt = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    def __del__(self):
        self.capt.release()

    def get_frame(self):
        retval, frame = self.capt.read()
        frame_flip = cv2.flip(frame, 1)
        retval, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()