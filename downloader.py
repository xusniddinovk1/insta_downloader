import requests
import json


def insta_downloader(video_url: str):
    url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

    payload = {"url": video_url}
    headers = {
        "x-rapidapi-key": "476013b9aemsh624b1818a0fccf4p190c87jsn4bab67de2049",
        "x-rapidapi-host": "auto-download-all-in-one.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    res = json.loads(response.text)
    if res.get("error"):
        return False

    return res.get('medias')[0].get('url')

# print(insta_downloader("https://www.tiktok.com/@yeuphimzz/video/7237370304337628442"))
