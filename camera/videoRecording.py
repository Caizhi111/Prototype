import os
os.system('ffmpeg -t 30 -f v4l2 -framerate 25 -video_size 640x80 -i /prototyping/camera -t 300 output.mkv')
