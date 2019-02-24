key = '0DLTIn76i0DQgGg8zZ5OG1WBAcbDEmf1'
city = 'changsha'
url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak={}'.format(city, key)
print(url)

import requests
from pprint import pprint

response = requests.get(url)
weather_dicts = response.json()

pprint(weather_dicts)

weather_data = weather_dicts['results'][0]['weather_data']
print(weather_dicts['results'][0]['currentCity'])
for each_item in weather_data:
    print(each_item['date'])
    print(each_item['temperature'])
    print(each_item['weather'])
    print(each_item['wind'])


def search_place(hot_place='饭店', city=city):
    url = 'http://api.map.baidu.com/place/v2/search?q={}&region={}&output=json&ak={}'.format(hot_place, city, key)
    response = requests.get(url)
    places_dicts = response.json()
    pprint(places_dicts), type(places_dicts)
    print('Total:{}'.format(len(places_dicts['results'])))
    for index, each_item in enumerate(places_dicts['results']):
        print(index + 1, each_item['name'])
        print(each_item['address'] if 'address' in each_item else 'Address None')
        print(each_item['telephone'] if 'telephone' in each_item else 'telephone None')


search_place(hot_place='饭店', city='上海')
