
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from dotenv import load_dotenv
import os
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

try:
    my_thing.read()

except KeyError:
    print("nothing")


video_prop = my_thing.find_or_create_property("video", PropertyType.VIDEO)


my_thing.update_property_http(video_prop, "/home/pi/Prototype/cavideo\/1.mp4")
