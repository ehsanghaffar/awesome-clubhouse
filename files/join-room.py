#
# Join a room with a given room id and user auth token.
# Author: Ehsan Ghaffar
# This file is part of the spacepy.


import requests

url = "https://www.clubhouseapi.com/api/join_channel"

token = "YOUR_TOKEN_HERE"

payload = "{\n\t\"channel\": \"m3lqLypG\"\n}\n"

headers = {
    "CH-Languages": "en-US",
    "CH-Locale": "en_US",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "CH-AppBuild": "2576",
    "CH-AppVersion": "1.0.0",
    "CH-UserID": "<id>",
    "User-Agent": "clubhouse/490 (iPhone; iOS 14.4; Scale/2.00)",
    "Connection": "alive",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Token " + token
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
