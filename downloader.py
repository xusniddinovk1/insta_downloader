import os
import requests
import json


def insta_downloader(video_url: str):
    url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

    payload = {"url": video_url}
    headers = {
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
        "x-rapidapi-host": os.getenv('RAPIDAPI_HOST'),
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    res = json.loads(response.text)
    if res.get("error"):
        return False

    return res.get('medias')[0].get('url')
