from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType
from dotenv import load_dotenv
import os
import signal


load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

try:
    my_thing.read()

except KeyError:
    print("nothing")


prop = my_thing.find_property_by_name("hello")
print("property id is {}".format(prop.property_id))
prop = my_thing.read_property(prop.property_id)
a = my_thing.properties[prop.property_id]
print('--')
print(a.values)
print('--')
print(prop)

# Register our Keyboard handler to exit


def keyboard_interrupt_handler(signal_num):
    """Make sure we close our program properly"""
    print("Exiting...".format(signal_num))
    exit(0)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)
