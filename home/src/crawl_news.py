import requests
import json

MOYA_URL = "https://api.moya.ai/news?token=l2pfo3MOSrb7Uwnnad4IUl0uwUWUFA"

def make_categoryUrl(category):
    url = f"{MOYA_URL}&category={category}"
    return url

def get_data(url):
    response = requests.get(url)
    if response.status_code==200:
        datas = response.content.decode("utf-8")
        json_datas = json.loads(datas)

        return json_datas["datas"]

def main():
    url = make_categoryUrl("경제")
    datas = get_data(url)
    return datas
    



 


