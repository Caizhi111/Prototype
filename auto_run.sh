#!/bin/bash
python3 serial_to_dcdhub2.py &
python3 camera/videoRecording.py &
python3 wechat_sending.py &
python3 web/server.py &