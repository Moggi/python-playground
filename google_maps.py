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

main_api = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    print('=== STARTING ===')
    address = input('Address: ')

    if address == 'q' or address == 'quit' or address == 'exit':
        break

    api_param = {
        'address': address,
        'key': api_key,
    }

    url = main_api + urllib.parse.urlencode( api_param )

    json_data = requests.get(url).json()

    # pprint(json_data['results'])

    json_status = json_data['status']

    print(url)
    print('API Status: ' + json_status)

    if json_status == 'OVER_QUERY_LIMIT':
        print('Too many queries. Stoping for now')
        break

    for result in json_data['results']:
        formatted_address = result['formatted_address']
        location_latlng = str(result['geometry']['location']['lat']) +','+ str(result['geometry']['location']['lng'])
        google_place_id = result['place_id']

        print()
        print('Address Name: ' + formatted_address)
        print('Location: ' + location_latlng)
        print('Place ID: ' + google_place_id)
