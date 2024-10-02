import os
import requests
import json

# Get all API keys from env
WEBEX_KEY = os.getenv('WEBEX_KEY')
GRAPHHOPPER_KEY = os.getenv('GRAPHHOPPER_KEY')
OPENWEATHERMAP_KEY = os.getenv('OPENWEATHERMAP_KEY')

def geocode(location):
    '''
    Retrieves the coordinates for a given location string
    Returns coordinates as a list: [lat, lon]
    '''
    # Define base URL
    base_url = 'https://graphhopper.com/api/1'

    # Prepare the parameters for request
    params = {
        'key': GRAPHHOPPER_KEY,
        'q': location
    }
    
    # Perform the request
    resp = requests.get(
        base_url + '/geocode',
        params=params
    )

    # Check if request was succesful
    if resp.status_code != 200:
        return

    resp_data = resp.json()

    # Check if result is empty
    if len(resp_data['hits']) == 0:
        return
    
    # Extract data from JSON
    lat = resp_data['hits'][0]['point']['lat']
    lon = resp_data['hits'][0]['point']['lng']

    coords = [lat, lon]

    return coords

def get_weather(lat, lon, units='metric', lang='en'):
    '''
    Retrives weather information for location identified by lat and lon
    Returns: a dict with the following keys:
        'temp',
        'feels_like',
        'humidity',
        'description',
        'icon'
    '''

    # Define base URL
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    # Prepare parameters
    # lat={lat}&lon={lon}&appid={API key}
    params = {
        'appid': OPENWEATHERMAP_KEY,
        'lat': lat,
        'lon': lon,
        'units': units,
        'lang': lang
    }

    # Perform the request
    resp = requests.get(
        base_url,
        params=params
    )

    # Check if request was successful
    if resp.status_code != 200:
        return

    # Extract data from JSON
    json_data = resp.json()

    result = {
        'temp': json_data['main']['temp'],
        'feels_like': json_data['main']['feels_like'],
        'humidity': json_data['main']['humidity'],
        'description': json_data['weather'][0]['description'],
        'icon': json_data['weather'][0]['icon']
    }

    return result


def get_last_message(roomId):
    '''
    Retrieve the last message from the Webex space.
    '''

    # Define base URL
    base_url = 'https://webexapis.com/v1/messages'

    # Define parameters
    params = {
        'roomId': roomId,
        'max': 1
    }

    # Define headers
    headers = {
        'Authorization': 'Bearer ' + WEBEX_KEY
    }

    # Perform the API call
    resp = requests.get(
        base_url,
        params=params,
        headers=headers
    )

    # Check if the call was successful
    json_data = resp.json()

    # Extract the data from JSON

    return json_data['items'][0]



# coords = geocode('Mexico city')
# weather = get_weather(coords[0], coords[1])
# print(json.dumps(weather, indent=4))


print(get_last_message('Y2lzY29zcGFyazovL3VzL1JPT00vMzA0MWM3MzAtN2ZkYS0xMWVmLTg1ZWQtM2QzZThkNTU3MjJl'))


# while True:
#     pass
    # retrieve the last message from the room - build a function 
    
    # check if the last message in the room starts with /

    # strip the /

    # request coordinates vie geocoding API - already have a function

    # retrieve weather data via OpenWeatherMap API - will need a function

    # respond to Webex message with weather info - build a function

    # wait a little