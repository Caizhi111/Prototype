#!/bin/bash
python3 /home/pi/Prototype/serial_to_dcdhub2.py &
python3 /home/pi/Prototype/camera/videoRecording.py &
python3 /home/pi/Prototype/web/static/wechat_sending.py &
python3 /home/pi/Prototype/web/server.py &
