import json
import urllib2
from flask import Flask, request
from cors import CORS

import flyscanner

app_url = '/matlaczm/app'
app = Flask(__name__)
CORS(app)

api_key = 'ah197772008646643372222298324115'


def get_api_key():
    return api_key


@app.route(app_url + '/event/')
def get_event():
    if request.method == 'GET':
        query = request.args['q']
        token = 'CAAKMrAl97iIBAMw2HbloZAGrjpoyi8hQ6fMUtACOV6rerZBglvSy5f6OtrE4xPaiOOZA7pVBZBLmZAHwGIr5cj8d7uKIvAExQJYdcgnhT6TPamZBoLwusTIXFdHCFDfhftfxUSsTf2U9ZBv3WZBKA1jZAhXrJ1uhwCUna068rqTcrZB3a6Pq4ml6haBdY6eSWd5brFIZBLE1Bx9VlNRcmvjnyrdCEJTQPmHvGEaWNP7nQgrwAZDZD'
        url = 'https://graph.facebook.com/v2.5/search?access_token={}&q={}&type=event'.format(token, query)
        events = urllib2.urlopen(url).read()
        events = json.loads(events)

        return json.dumps(events)


@app.route(app_url + '/event/<id>')
def get_event_by_id(id):
    if request.method == 'GET':
        token = 'CAAKMrAl97iIBAMw2HbloZAGrjpoyi8hQ6fMUtACOV6rerZBglvSy5f6OtrE4xPaiOOZA7pVBZBLmZAHwGIr5cj8d7uKIvAExQJYdcgnhT6TPamZBoLwusTIXFdHCFDfhftfxUSsTf2U9ZBv3WZBKA1jZAhXrJ1uhwCUna068rqTcrZB3a6Pq4ml6haBdY6eSWd5brFIZBLE1Bx9VlNRcmvjnyrdCEJTQPmHvGEaWNP7nQgrwAZDZD'
        url = 'https://graph.facebook.com/v2.5/{}?access_token={}'.format(id, token)
        event = urllib2.urlopen(url).read()
        event = json.loads(event)
        return json.dumps(event)


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
