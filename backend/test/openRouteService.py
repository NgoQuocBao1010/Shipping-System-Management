import requests
import pprint

body = {"coordinates": [[105.739714, 10.0184892], [105.78839074112506, 10.01792665]]}

headers = {
    "Accept": "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
    "Authorization": "5b3ce3597851110001cf6248f8c35fd1e82d4754933bf5d8fea33263",
    "Content-Type": "application/json; charset=utf-8",
}
call = requests.post(
    "https://api.openrouteservice.org/v2/directions/driving-car/geojson",
    json=body,
    headers=headers,
)

print(call.status_code, call.reason)
pprint.pprint(call.text)
