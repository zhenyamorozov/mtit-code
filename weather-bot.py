import os
import requests

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
    
    lat = resp_data['hits'][0]['point']['lat']
    lon = resp_data['hits'][0]['point']['lng']

    coords = [lat, lon]

    return coords

def get_weather(lat, lon, units='metric'):
    '''
    Retrives weather information for location identified by lat and lon
    Returns: TODO
    '''


    return



# define API base URLs - inside functions

# while True:
#     pass
    # check if the last message in the room starts with / - build a function

    # strip the /

    # request coordinates vie geocoding API - already have a function

    # retrieve weather data via OpenWeatherMap API - will need a function

    # respond to Webex message with weather info - build a function

    # wait a little