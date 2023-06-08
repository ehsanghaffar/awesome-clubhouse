import requests
import time
import random

url = "https://www.clubhouseapi.com/api/join_channel"

channel = "myyW812a"

tokens = [
    "3b3ddf2203e79b21e1cb002bc42f5e4e28e95975",
    "da74178ea8fab9e613746d7c013a306d525cda37"
]

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'CH-AppBuild': '2029',
    'CH-AppVersion': '23.02.07',
    'User-Agent': 'clubhouse/2029 (iPhone; iOS 16.3; Scale/3.00)',
    'Connection': 'close',
    'Content-Type': 'application/json; charset=utf-8',
}

def join_channel(token, channel, attribution_source="feed", attribution_details="eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0="):
    data = {
        "channel": channel,
        "attribution_source": attribution_source,
        "attribution_details": attribution_details
    }
    headers['Authorization'] = 'Token ' + token

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response

for token in tokens:
    join_channel(token, channel)
    time.sleep(10)