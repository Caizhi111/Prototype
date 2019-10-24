#!/bin/bash
import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", 'serial_to_dcdhub2.py'])
sleep(y)
subprocess.Popen(["python", 'videoRecording.py'])
#sleep (y)
#subprocess.Popen(["python", '3.py'])
#sleep (y)
#subprocess.Popen(["python", '4.py'])
