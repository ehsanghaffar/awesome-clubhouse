#
# Join a room with a given room id and user auth token.
# Author: Ehsan Ghaffar
# This file is part of the spacepy.
import requests
import json


api_url = "https://www.clubhouseapi.com/api/"

token = "YOUR_TOKEN_HERE"

channel_id = ""


def join_room(t, url, ch):
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
    end_point = url + 'join_channel'

    payload = {
        "channel": ch
    }

    response = requests.request(
        "POST", end_point, json=payload, headers=headers)
    room_res = response.json()
    dumped_res = json.dumps(room_res, indent=2)
    print(room_res)


# call join rooom function
join_room(token, api_url, channel_id)
