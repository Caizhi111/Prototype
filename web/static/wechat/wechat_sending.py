from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType, Property
from dotenv import load_dotenv
import os
import signal
from time import sleep
import datetime
import itchat
from googleplaces import GooglePlaces
import googlemaps
import sys
from imp import reload


reload(sys)

END_DATE1 = datetime.datetime.now() + datetime.timedelta(hours = 24)
END_DATE = END_DATE1.replace(microsecond=0)
START_DATE = END_DATE - datetime.timedelta(hours = 100)
    #print(START_DATE)
    #print(END_DATE)

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

# prop = my_thing.properties[prop1.property_id]
# print('--')
# print(prop.values[0][1:4])

itchat.auto_login(hotReload=True,enableCmdQR=2)

users = itchat.search_friends(name = '刘益伶')
#contact = u'ai'
contact_person = users[0]['UserName']
print(contact_person)



# else:
    # print("I'm fine")
# Register our Keyboard handler to exit

def keyboard_interrupt_handler(signal_num):
    """Make sure we close our program properly"""
    print("Exiting...".format(signal_num))
    exit(0)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)


class GoogleMaps(object):
    """提供google maps服务"""

    def __init__(self):

        self._GOOGLE_MAPS_KEY = "FIXME"
        self._Google_Places = GooglePlaces(self._GOOGLE_MAPS_KEY)
        self._Google_Geocod = googlemaps.Client(key=self._GOOGLE_MAPS_KEY)

    def _text_search(self, query, language=None, location=None):
        """
        根据搜索字符串,请求google API传回推荐的列表
        :param query: 搜索字符串
        :param language: 语言
        :param location: 地区筛选
        :return:
        """
        # lat_lng = {"lat": "22.5745761", "lng": "113.9393772"}
        # 经纬度附近搜索
        # text_query_result = self.self._Google_Places.text_search(query='Gong Yuan', lat_lng=lat_lng)
        # location 为人可认识的名称
        # text_query_result = self.self._Google_Places.text_search(query='Tang Lang Shan', location='shenzhen')
        # 指定语言搜索
        text_query_result = self._Google_Places.text_search(query=query, language=language, location=location)
        return text_query_result.places

    def _reverse_geocode(self, lat, lng, language=None):
        """
        根据经纬度请求google API获取坐标信息,返回信息
        :param lat: 纬度
        :param lng:经度
        :param language:语言
        :return:
        """
        # 根据经纬度获取地址信息 pincode
        list_reverse_geocode_result = self._Google_Geocod.reverse_geocode((lat, lng), language=language)
        # print json.dumps(list_reverse_geocode_result, indent=4)
        return list_reverse_geocode_result

    def _return_reverse_geocode_info(self, lat, lng, language=None):
        """
        整理信息
        :param lat:纬度
        :param lng:经度
        :param language:语言
        :return:
        """
        list_reverse_geocode = self._reverse_geocode(lat, lng, language=language)
        if list_reverse_geocode:
            city = ''
            pincode = ''
            route = ''
            neighborhood = ''
            sublocality = ''
            administrative_area_level_1 = ''
            country = ''
            street_number = ''
            # 全名地址
            formatted_address = list_reverse_geocode[0]['formatted_address']
            for address_info in list_reverse_geocode[0]['address_components']:
                # 城市标识为locality
                if 'locality' in address_info['types']:
                    city = address_info['long_name']
                # 邮政编码标识为postal_code
                elif 'postal_code' in address_info['types']:
                    pincode = address_info['long_name']
                # 街道路
                elif 'route' in address_info['types']:
                    route = address_info['long_name']
                # 相似地址名
                elif 'neighborhood' in address_info['types']:
                    neighborhood = address_info['long_name']
                # 地区名
                elif 'sublocality' in address_info['types']:
                    sublocality = address_info['long_name']
                # 省份
                elif 'administrative_area_level_1' in address_info['types']:
                    administrative_area_level_1 = address_info['long_name']
                # 国家
                elif 'country' in address_info['types']:
                    country = address_info['long_name']
                # 门牌号
                elif 'street_number' in address_info['types']:
                    street_number = address_info['long_name']
            return {'city': city, 'pincode': pincode, 'route': route, 'neighborhood': neighborhood,
                    'sublocality': sublocality, 'administrative_area_level_1': administrative_area_level_1,
                    'country': country, 'formatted_address': formatted_address, 'street_number': street_number}
        else:
            return None

    def get_pincode_city(self, lat, lng, language=None):
        """
        根据经纬度获取该地区详细信息
        :param lat: 纬度
        :param lng: 经度
        :return:
        """
        reverse_geocode_info = self._return_reverse_geocode_info(lat, lng, language=language)
        if reverse_geocode_info:
            return {'city': reverse_geocode_info['city'], 'pincode': reverse_geocode_info['pincode']}
        else:
            return None

    def get_address_recommendation(self, query, language=None, location=None):
        """
        获取输入地址的推荐地址(最多返回5个)
        :param query: 搜索地址名称
        :param language: 语言
        :param location: 地区筛选
        :return:
        """
        return_size = 5
        list_return_info = list()
        list_places_text_search_result = self._text_search(query=query, language=language, location=location)
        # 默认返回5条数据
        if len(list_places_text_search_result) > return_size:
            list_places_text_search_result = list_places_text_search_result[:return_size]
        for place in list_places_text_search_result:
            result_geocode = self._return_reverse_geocode_info(place.geo_location['lat'], place.geo_location['lng'], language=language)
            # 数据不为空
            if result_geocode:
                # 地点全路径加上地点名
                result_geocode['formatted_address'] = '{} {}'.format(place.name, result_geocode['formatted_address'])
                result_geocode['place_name'] = place.name
                # 经纬度
                result_geocode['lat'] = '{}'.format(place.geo_location['lat'])
                result_geocode['lng'] = '{}'.format(place.geo_location['lng'])
                list_return_info.append(result_geocode)
        return list_return_info


#Location =
#Videolink =
#itchat.send(u'FIXME%d, %s, be careful'%(Location, Videolink), toUserName='username')\

#Modify here

count = 0
# while count < 1:
while(True):
    #读取dcdhub上面的gps数据， 哪段时间里面的数据
    prop1 = my_thing.read_property('gps-92d6', from_ts, to_ts)
    prop = my_thing.properties[prop1.property_id]
    #print('--')
    # print(prop.values[0][1])
    # loc = *prop.values[0][1:3], sep=','

    prop2 = my_thing.read_property('euler-7b32', from_ts, to_ts)
    prop_EULER = my_thing.properties[prop2.property_id]
    #print('--')



    pos = prop_EULER.values[-1]
    print(pos[1])
    print(pos[2])
    print(pos[3])
    print("Condition not Satisfied")

    if abs(float(pos[2]))> 60  or abs(float(pos[3])) > 60 :
        print("Condition Satisfied")
    #itchat.send(message_location, Videolink, toUserName = contact_person)

        if __name__ == '__main__':
        # 使用实例
            import json
            gmaps = googlemaps.Client(key="AIzaSyDviAQA75uBKrDAHylBtMBkUxztPAUhKeg")
            reverse_geocode_results = gmaps.reverse_geocode((prop.values[-1][1], prop.values[-1][2]))
            print (reverse_geocode_results[0]["formatted_address"])

        Videolink = "http://145.94.153.90:5000/static/video/video.mp4"
        message_content_1 = "There is a likely accident happened to the wheelchair user, the location is as follows:"
        message_content_2 = reverse_geocode_results[0]["formatted_address"]
        message_content_3 = "Check the recorded video:" + Videolink

        itchat.send(message_content_1, toUserName = contact_person)
        itchat.send(message_content_2, toUserName = contact_person)
        itchat.send(message_content_3, toUserName = contact_person)
    #itchat.send(message_content, toUserName = contact_person)
        itchat.run(blockThread=False)
        continue
    print("fuck")
    sleep(1)
