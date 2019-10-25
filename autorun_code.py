#!/bin/bash
import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", '1.py'])
sleep(y)
subprocess.Popen(["python", '2.py'])
sleep (y)
subprocess.Popen(["python", '3.py'])
sleep (y)
subprocess.Popen(["python", '4.py'])
