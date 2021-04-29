import base64
import os
import sys
import time
from datetime import datetime

import requests


def discord(message):
    url = os.environ["DISCORD_WEBHOOK_URL"]
    payload = {"content": message}

    with requests.Session() as s:
        s.headers.update({"Content-Type": "application/x-www-form-urlencoded"})
        return s.post(url, data=payload)


def hello_pubsub(event, context):
    try:
        curr = datetime.fromtimestamp(time.time())
        discord(curr)
    except:
        print(str(sys.exc_info()))
