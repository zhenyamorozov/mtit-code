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
    
    # Extract data from JSON
    lat = resp_data['hits'][0]['point']['lat']
    lon = resp_data['hits'][0]['point']['lng']

    coords = [lat, lon]

    return coords

def get_weather(lat, lon, units='metric', lang='en'):
    '''
    Retrives weather information for location identified by lat and lon
    Returns: TODO
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


print(get_weather(52.510885, 13.3989367))


# define API base URLs - inside functions

# while True:
#     pass
    # check if the last message in the room starts with / - build a function

    # strip the /

    # request coordinates vie geocoding API - already have a function

    # retrieve weather data via OpenWeatherMap API - will need a function

    # respond to Webex message with weather info - build a function

    # wait a little