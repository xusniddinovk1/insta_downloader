import requests
import json


def insta_downloader(video_url: str):
    url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

    payload = {"url": video_url}
    headers = {
        "x-rapidapi-key": "b3aa1cd380msh421797429984087p1d1f7ajsn754b83a84821",
        "x-rapidapi-host": "auto-download-all-in-one.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    res = json.loads(response.text)

    try:
        if res.get("error"):
            return False

        return res.get("media")[0].get("url")
    except NameError:
        return False
