import HTMLParser
import json
import urllib2

from flask import Flask, request

import config
import facebook
import flyscanner
from cors import CORS
from transits import get_connections

# Set up Flask API
app_url = '/matlaczm/app'
app = Flask(__name__)
app.debug = True

airports_db = open('airports.dat', 'rb+')
airports = airports_db.read()

CORS(app)

# Facebook client
facebook_app_id = config.FACEBOOK.get('APPLICATION_ID')
facebook_app_secret = config.FACEBOOK.get('APPLICATION_SECRET')

# facebook_access_token = facebook.get_app_access_token(app_id=facebook_app_id, app_secret=facebook_app_secret)
facebook_client = facebook.GraphAPI(access_token='')

# temporary acc_token hack
facebook_client.access_token = 'CAAYcd83pBg4BAKV6wvZAJH4xv2U1WE7qDSo0RPe4XP5mcZBwwaORiAmjKj95SCxIXntDeBDGGnIgSWS9nuuzqO3udyxvenzFaF9wmcKucxTZAgp4TwUYfMbYpH1aSTT5yNA2uu2ZAasf3vanyz9V2R8XNcRK9meMgULAV7MGJHStJYWjM2cWk7ZA41LVAJ1UZD'


@app.route(app_url + '/event/')
def get_event():
    if request.method == 'GET':
        query_string = request.args['q']
        params = {
            'q': query_string,
            'type': 'event'
        }

        search_results = facebook_client.request(path='search', args=params)
        parsed_results = list()

        for event in search_results.get('data', []):
            parsed_event = {
                'thumbnail': 'https://graph.facebook.com/{0}/picture?access_token={1}'.format(event['id'],
                                                                                              facebook_client.access_token)
            }
            for key in config.EVENT.get('FIELDS', []):
                if event.has_key(key):
                    parsed_event.update({key: event[key]})

            if parsed_event != {}:
                parsed_results.append(parsed_event)
        return json.dumps(parsed_results[:config.EVENT.get('LIMIT', 10)])


@app.route(app_url + '/event/<id>/')
def get_event_by_id(id):
    if request.method == 'GET':
        return json.dumps(facebook_client.get_object(id=id, args={'access_token': facebook_client.access_token}))


@app.route(app_url + '/hotel/')
def hotels():
    if request.method == 'GET':
        city = request.args['city']
        checkin = request.args['checkin']
        checkout = request.args['checkout']
        guests = request.args['guests']
        rooms = request.args['rooms']
        return flyscanner.get_hotels(city, checkin, checkout, guests, rooms)


@app.route(app_url + '/to/')
def transit():
    if request.method == 'GET':
        event_city = request.args['event_city']
        event_country = request.args['event_country']
        start_city = request.args['start_city']
        start_country = request.args['start_country']
        out_time = request.args['out_time']
        in_time = request.args['in_time']
        return get_connections(event_city, event_country, start_city, start_country, out_time, in_time)

@app.route(app_url + '/airports/')
def return_airports():
    return airports

@app.route(app_url + '/airports/<id>/')
def airport(id):
    city = urllib2.urlopen("https://www.wolframcloud.com/objects/caf4da56-9cc9-4673-8bc0-63a1371180ac?code="+id).read()
    city = city[17:]
    city = city[:-3]

    city = city.split("\"")
    print city

    return json.dumps({'city': city[3], 'country': city[-2]})


if __name__ == '__main__':
    app.run()
