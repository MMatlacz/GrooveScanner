import json

import requests

import config
import urllib


class AirportAPI:
    api_key = config.AIRPORT.get('API_KEY')
    endpoint = 'https://airport.api.aero/airport/?user_key={token}'

    @staticmethod
    def get_airports(long=None, lat=None):
        args = {'user_key': AirportAPI.api_key}
        url = 'https://airport.api.aero/airport/'
        if long and lat:
            url += "nearest/{0}/{1}/".format(long, lat)
        url += '?' + urllib.urlencode(args)

        airports_request = requests.get(url, headers={'content-type': 'application/json'})
        response_text = airports_request.text.replace("callback(", "")[:-1]

        return json.loads(response_text)['airports']


