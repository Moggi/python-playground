import sys
import urllib.parse
import requests
from pprint import pprint

if len(sys.argv) > 1:
    api_key = str(sys.argv[1])
    if len(sys.argv) > 2:
        api_key = str(sys.argv[2])
else:
    print ("Usage: %s api_key" % sys.argv[0])
    sys.exit()

main_api = "http://api.openweathermap.org/data/2.5/weather?"
units = 'metric'

while True:
    print('=== STARTING ===')
    address = input('Address: ')

    if address == 'q' or address == 'quit' or address == 'exit':
        break

    api_param = {
        'q': address,
        'APPID': api_key,
        'units': units,
    }

    url = main_api + urllib.parse.urlencode( api_param )

    json_data = requests.get(url).json()

    # pprint(json_data)

    json_status = str(json_data['cod'])

    print(url)
    print('API Status: ' + json_status)

    if json_status != '200':
        print('Something got wrong. Stoping for now')
        break

    location_latlng = str(json_data['coord']['lat']) +','+ str(json_data['coord']['lon'])
    openweather_id = str(json_data['id'])

    print()
    print('Address Name: ' + json_data['name'])
    print('Temperature: ' + str(json_data['main']['temp']))
    print('Weather: ' + str(json_data['weather'][0]['description']))
    print('Location: ' + location_latlng)
    print('Place ID: ' + openweather_id)
