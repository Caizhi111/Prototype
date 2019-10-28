from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType, Property
from dotenv import load_dotenv
import os
import signal
import datetime
import sys
from imp import reload

reload(sys)


END_DATE1 = datetime.datetime.now()
END_DATE = END_DATE1.replace(microsecond=0)
START_DATE = END_DATE - datetime.timedelta(hours = 100)
print(START_DATE)
print(END_DATE)

from datetime import datetime
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
from_ts = datetime.timestamp(datetime.strptime(str(START_DATE), DATE_FORMAT))*1000
to_ts = datetime.timestamp(datetime.strptime(str(END_DATE), DATE_FORMAT))*1000

load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

try:
    my_thing.read()

except KeyError:
    print("nothing")

prop2 = my_thing.read_property('euler-7b32', from_ts, to_ts)
prop_euler = my_thing.properties[prop2.property_id]
print(prop_euler.values[1][2][3])

if prop_euler.value[1]>0:
    print(prop_euler.value[1])
