# final project for CS50 Python
# Author: Jerome Schmutz

import requests

api_key = "ewghalzgdltowqhen8pwx0nv9b3oh37aloeo7icj"

url_base = "https://www.meteosource.com/api/v1/free"


# this function return a list of 10 available locations based on a simple string
def get_list_location(text):
    url = url_base + "/find_places"
    parameters = {'key': api_key,
                  'text' : text}
    try:
        data = requests.get(url, parameters).json()
    except:
        pass
    else:
        return data


# this function returns the daily forecast for a specific location in parameter
def get_week_data(location):
    location = location.replace(" ", "-")
    url = url_base + "/point"
    parameters = {'key': api_key,
                  'place_id': location,
                  'sections': 'daily',
                  'units': 'metric'}
    try:
        data = requests.get(url, parameters).json()
    except:
        pass
    else:
        return data

# this function returns the hourly forecast for a specific location in parameter
def get_day_data(location):
    location = location.replace(" ", "-")
    url = url_base + "/point"
    parameters = {'key': api_key,
                  'place_id': location,
                  'sections': 'hourly',
                  'units': 'metric'}
    try:
        data = requests.get(url, parameters).json()
    except:
        pass
    else:
        return data