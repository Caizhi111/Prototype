
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType, Property
from dotenv import load_dotenv
import os
import signal
import serial
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

ser = serial.Serial(
    port = os.environ['SERIAL'],
    baudrate = 115200,
    timeout = 2)

try:
    my_thing.read()

except KeyError:
    print("nothing")

gps = my_thing.find_or_create_property('GPS_values', PropertyType.TWO_DIMENSIONS)

gps.update_values('101', '102')


def keyboard_interrupt_handler(signal_num):
    exit(0)

signal.signal(signal.SIGINT, keyboard_interrupt_handler)
