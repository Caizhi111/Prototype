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

prop1 = my_thing.read_property('gps-92d6', from_ts, to_ts)
prop = my_thing.properties[prop1.property_id]

if prop.value[1]>0:
    print(prop[1][2])
