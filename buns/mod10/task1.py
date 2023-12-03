import requests
import json
response = requests.get("https://swapi.dev/api/starships/?search=Millennium%20Falcon")
data = response.json()
pilots_info = []
for pilot_url in data['results'][0]['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    homeworld_response = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_response.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_info': homeworld_data
    }
    pilots_info.append(pilot_info)

millennium_falcon_info = {
    'name': data['results'][0]['name'],
    'max_speed': data['results'][0]['max_atmosphering_speed'],
    'class': data['results'][0]['starship_class'],
    'pilots': pilots_info
}
print(json.dumps(millennium_falcon_info, indent=2))
with open('millennium_falcon_info.json', 'w') as file:
    json.dump(millennium_falcon_info, file, indent=2)