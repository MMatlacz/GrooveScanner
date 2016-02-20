import os, sys
import config
import json
import urllib2
import flyscanner
import facebook

from flask import Flask, request
from cors import CORS

# Set up Flask API
app_url = '/matlaczm/app'
app = Flask(__name__)
app.debug = True

CORS(app)

# Facebook client
facebook_app_id = config.FACEBOOK.get('APPLICATION_ID')
facebook_app_secret = config.FACEBOOK.get('APPLICATION_SECRET')

facebook_access_token = facebook.get_app_access_token(app_id=facebook_app_id, app_secret=facebook_app_secret)
facebook_client = facebook.GraphAPI(access_token=facebook_access_token)

# temporary acc_token hack
facebook_client.access_token = 'CAAKMrAl97iIBAMw2HbloZAGrjpoyi8hQ6fMUtACOV6rerZBglvSy5f6OtrE4xPaiOOZA7pVBZBLmZAHwGIr5cj8d7uKIvAExQJYdcgnhT6TPamZBoLwusTIXFdHCFDfhftfxUSsTf2U9ZBv3WZBKA1jZAhXrJ1uhwCUna068rqTcrZB3a6Pq4ml6haBdY6eSWd5brFIZBLE1Bx9VlNRcmvjnyrdCEJTQPmHvGEaWNP7nQgrwAZDZD'


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



    '''
    market = request.args['market']
    currency = request.args['currency']
    locale = request.args['locale']
    originPlace = request.args['originPlace']
    destinationPlace = request.args['destinationPlace']
    outboundPartialDate = request.args['outboundPartialDate']
    inboundPartialDate = request.args['inboundPartialDate']
    return flyscanner.return_grid(market, currency, locale, originPlace, destinationPlace, outboundPartialDate,
                                  inboundPartialDate)'''


if __name__ == '__main__':
    app.run()
