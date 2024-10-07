import os
import requests
import json
import time

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
    Retrieves the last message from the Webex space.
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

    # Check if request was successful
    if resp.status_code != 200:
        return

    # Check if the call was successful
    json_data = resp.json()

    # Extract the data from JSON

    return json_data['items'][0]


def post_message(roomId, text):
    '''
    Posts a message into Webex space
    '''

    # Define base URL
    base_url = 'https://webexapis.com/v1/messages'

    # Define body
    body = {
        'roomId': roomId,
        'text': text
    }

    # Define headers
    headers = {
        'Authorization': 'Bearer ' + WEBEX_KEY
    }

    # Perform the request
    resp = requests.post(
        base_url,
        headers=headers,
        json=body
    )

    # Check if request was successful
    if resp.status_code != 200:
        return

    # Extract the result
    json_data = resp.json()

    return json_data


weather_icons = {
    '01': '☀️',
    '02': '⛅',
    '03': '☁️',
    '04': '☁️',
    '09': '🌧️',
    '10': '🌦️',
    '11': '⛈️',
    '13': '❄️',
    '50': '🌫️'
}

print('Welcome to the Webex Weather Bot! ')
print('WWB lets you request weather information for any place in the world!')
roomId = input('Please enter the ID of the room to monitor: ')

# post_message(roomId, 'Welcome to the weather bot. Ask about weather with a command like this: /Berlin')


while True:
    # Get the last message in the room
    last_message = get_last_message(roomId)

    # Check if message is a command
    if last_message['text'][0] == '/':

        # Strip the leading /
        location = last_message['text'].strip('/')

        # Retrieve coordinates
        coords = geocode(location)

        if not coords:
            post_message(roomId, 'The location is not recognized.')
            continue

        # Retrieve weather
        weather = get_weather(coords[0], coords[1])

        if not weather:
            post_message(roomId, 'Could not get weather')
            continue

        # Post weather
        icon = weather_icons[weather['icon'].strip('dn')]
        post_message(
            roomId,
            f'''{icon}  {weather['description']}
Temperature: {weather['temp']}
Feels like: {weather['feels_like']}
Humidity: {weather['humidity']}'''
        )

    time.sleep(5)

# Application flow:

# ask user for room to monitor

# while True:

    # retrieve the last message from the room - build a function 
    
    # check if the last message in the room starts with /

    # strip the /

    # request coordinates vie geocoding API - already have a function

    # retrieve weather data via OpenWeatherMap API - will need a function

    # respond to Webex message with weather info - build a function

    # wait a little