import googlemaps
from googlemaps import Client
import json
from . import Schedule_db
import requests


#Google place api key
API_KEY = "AIzaSyA3kdNaHOIsrsRonGCFBfrEPOtn6AezLb0"

class Place:
    def  __init__(self, includedTypes, radius, address):
        geometry = self.get_geometry(address)

        self.place_data = {
                "includedTypes": [includedTypes],
                "maxResultCount": 10,
                "rankPreference": "POPULARITY",   #DISTNACE OR POPULARITY
                "locationRestriction": {
                    "circle": {
                        "center": {
                            "latitude": geometry['lat'],
                            "longitude": geometry['lng']},
                        "radius": radius               #반경은 0.0 이상 50000.0 이하
                        }
                    }
                }

    #google place에서 id만 추출
    def get_id(self):
        client = Client(key=API_KEY)
        response = requests.post(
                "https://places.googleapis.com/v1/places:searchNearby",
                headers={
                    "Content-Type": "application/json",
                    "X-Goog-Api-Key": API_KEY,
                    "X-Goog-FieldMask": "places.name"
                    },
                json=self.place_data)
        if response.status_code == 200:
            return response.json()
        else:
            return False
    
    #google maps에서 좌표 추출
    def get_geometry(self, address):
        # 클라이언트 객체 생성
        client = Client(key=API_KEY)
        
        # 주소를 지도 형식으로 변환
        location = client.geocode(address)
        geometry = location[0]['geometry']['location']

        return geometry

def get_placeDetail(place_id):
    client = Client(key=API_KEY)
    response = requests.get(
            f"https://places.googleapis.com/v1/{place_id}",
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": API_KEY,
                "X-Goog-FieldMask": "*"
                }
            )
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code


