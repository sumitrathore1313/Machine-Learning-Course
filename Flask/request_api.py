# -*- coding: utf-8 -*-

import requests

location = "0.0,10.0"
datetime = "2016-12-25T01:04:08Z"
api_key = "b1b15e88fa797225412429c1c50c122a1"
url = "https://samples.openweathermap.org/pollution/v1/co/"+location+"/"+datetime+".json"

print(url)

data = {'appid': api_key}
response = requests.get(url=url, params=data)

print(response.json())
