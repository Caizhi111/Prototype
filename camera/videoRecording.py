# yiling
#import os
#os.system('ffmpeg -t 30 -f v4l2 -framerate 25 -video_size 640x80 -i /prototype/camera/ -t 300 output.mkv')

#yufei
import numpy as np
import cv2
import time
import os
import random
import sys

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

name = random.randint(0, 1000)
print(name)
if os.path.isdir(str(name)) is False:
    name = random.randint(0, 1000)
    name = str(name)

name = os.path.join(os.getcwd(), str(name))
print("ALl logs saved in dir:", name)
os.mkdir(name)


cap = cv2.VideoCapture(0)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


start = time.time()
video_file_count = 1
video_file = os.path.join(name, str(video_file_count) + ".mp4")
print("Capture video saved location : {}".format(video_file))

# Create a video write before entering the loop
out = cv2.VideoWriter(video_file, fourcc, 24, (640, 480))

while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)
        if time.time() - start > 10: #Every ten seconds save the video in created directory file
            start = time.time()
            video_file_count = 1
            video_file = os.path.join(name, str(video_file_count) + ".mp4")
            out = cv2.VideoWriter(video_file, fourcc, 24, (640, 480))
            # No sleeping! We don't want to sleep, we want to write
            # time.sleep(10)

        # Write the frame to the current video writer
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
