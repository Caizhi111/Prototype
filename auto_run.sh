<<<<<<< HEAD
=======
#!/bin/bash
python3 serial_to_dcdhub2.py &
python3 camera/videoRecording.py &
python3 web/wechat/wechat_sending.py &
python3 web/server.py &
>>>>>>> d3ac3febb12e9c3e6dadfa6f1ff8ecf32828fbc5
