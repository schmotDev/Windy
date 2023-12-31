# final project for CS50
# Author: Jerome Schmutz
# start Date: 30/12/2023

import requests

parameters = {'key': 'ewghalzgdltowqhen8pwx0nv9b3oh37aloeo7icj',
              'place_id': 'london'}

api_key = "ewghalzgdltowqhen8pwx0nv9b3oh37aloeo7icj"

url_base = "https://www.meteosource.com/api/v1/free/point"


# this function return the list of available locations
#  (not available with free API key )
def get_list_location():
    url = url_base + "/find_places"
    parameters = {'key': api_key}
    try:
        data = requests.get(url, parameters).json()
    except:
        pass
    else:
        return data


# this function returns the data for a specific location in parameter
def get_data(location):
    url = url_base
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



