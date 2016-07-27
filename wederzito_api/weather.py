import requests
import json

from consts import WEATHER_TAG_UNIFIER

API_KEY = '93c4d2f92ae0c40ee1ace84e5f7f5d08'  # TODO test key, put this variable in a smarter place
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q='


def weather_by_name(name):
    url = WEATHER_URL + name + '&APPID=' + API_KEY
    response = requests.get(url)
    json_response = json.loads(response.content)
    # {"coord":{"lon":2.35,"lat":48.85},"weather":[{"id":310,"main":"Drizzle",
    # "description":"light intensity drizzle rain","icon":"09n"}],"base":"stations",
    # "main":{"temp":293.58,"pressure":1018,"humidity":68,"temp_min":292.04,"temp_max":295.37},
    # "visibility":10000,"wind":{"speed":2.6,"deg":270},"clouds":{"all":0},"dt":1469653829,
    # "sys":{"type":1,"id":5615,"message":0.031,"country":"FR","sunrise":1469593136,"sunset":1469648065},
    # "id":2988507,"name":"Paris","cod":200}

    weather_id = json_response['weather'][0]['id']
    if json_response['sys']['country'] == 'FR':
        weather_id = 107

    return WEATHER_TAG_UNIFIER[weather_id]
