
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from dotenv import load_dotenv
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

try:
    my_thing.read()

except KeyError:
    print("nothing")


prop = my_thing.find_or_create_property("hello", PropertyType.VIDEO)
#video_prop.values = "C:\\Users\\11453\\Prototype\\1.mp4"

#print("video_prop.values is {}".format(video_prop.values))


clip = VideoFileClip("1.mp4")
duration = int(clip.duration)
prop.update_values([duration], file_name="1.mp4")
# my_thing.update_property_http(prop, "1.mp4")


print(','.join(map(str, prop.values[0])))
