import config
import json
import flyscanner
import facebook

from flask import Flask, request

from transits import get_connections
from cors import CORS

# Set up Flask API
app_url = '/matlaczm/app'
app = Flask(__name__)
app.debug = True

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
        parsed_results = [
            {key: event[str(key)] for key in config.EVENT.get('FIELDS', [])}
            for event in search_results.get('data', [])
            ]

        return json.dumps(parsed_results)


@app.route(app_url + '/event/<id>')
def get_event_by_id(id):
    if request.method == 'GET':
        return json.dumps(facebook_client.get_object(id=id, args={'access_token': facebook_client.access_token}))


@app.route(app_url + '/airports/')
def return_flights():
    return flyscanner.get_airports(request.args['q'])


@app.route(app_url + '/hotel/<city>')
def hotels(city):
    if request.method == 'GET':
        return flyscanner.get_hotels_ids(city)


@app.route(app_url + '/hotel/')
def hotel():
    if request.method == 'GET':
        id = request.args['id']
        checkin = request.args['checkin']
        checkout = request.args['checkout']
        guests = request.args['guests']
        rooms = request.args['rooms']
        print id, checkin, checkout, guests, rooms
        return json.dumps(flyscanner.get_hotels_list(id, checkin, checkout, guests, rooms))

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


if __name__ == '__main__':
    app.run()
