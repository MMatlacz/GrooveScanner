import urllib2

import itertools
from flask import json

market = "UK"
currency = "EUR"
locale = "en-GB"


def get_api_key():
    return 'ah197772008646643372222298324115'


def return_grid(market, currency, locale, originPlace, destinationPlace, outboundPartialDate, inboundPartialDate):
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/browsegrid/v1.0/{}/{}/{}/{}/{}/{}/{}?apiKey={}'.format(
        market, currency, locale, originPlace, destinationPlace, outboundPartialDate, inboundPartialDate, api_key
    )
    grid = urllib2.urlopen(url).read()
    grid = json.loads(grid)

    return json.dumps(grid)


def get_locales():
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey={}'.format(
        api_key
    )
    locales = urllib2.urlopen(url).read()
    locales = json.loads(locales)

    return json.dumps(locales)


def get_markets(locale):
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/reference/v1.0/countries/{}?apiKey={}'.format(
        locale, api_key
    )
    markets = urllib2.urlopen(url).read()
    markets = json.loads(markets)

    return json.dumps(markets)


def get_currencies():
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/reference/v1.0/currencies?apiKey={}'.format(
        api_key
    )
    currencies = urllib2.urlopen(url).read()
    currencies = json.loads(currencies)

    return json.dumps(currencies)


def get_airports(query):
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/{}/{}/{}/?query={}&apiKey={}'.format(
        market, currency, locale, query, api_key
    )
    currencies = urllib2.urlopen(url).read()
    currencies = json.loads(currencies)

    return json.dumps(currencies)


def get_hotels(query, checkin_date, checkout_date, guests, rooms):
    hotels = json.loads(get_hotels_ids(query))
    ids = []
    results = hotels['results']
    for result in results:
        ids.append(result['individual_id'])
    hotels = {}
    for id in ids:
        hotels['id'] = json.loads(get_hotels_list(id, checkin_date, checkout_date, guests, rooms))

    min_price = None
    id = None
    _hotel = None
    for price in hotels['id']['hotels_prices']:
        if price['agent_prices'][0]['price_total'] < min_price or min_price is None:
            min_price = price['agent_prices'][0]['price_total']
            id = price['id']

    for hotel in hotels['id']['hotels']:
        if hotel['hotel_id'] == id:
            _hotel = hotel
    _hotel['price'] = min_price
    return json.dumps(_hotel)


def get_hotels_ids(query):  # query is city name
    api_key = get_api_key()
    url = "http://partners.api.skyscanner.net/apiservices/hotels/autosuggest/v2/{}/{}/{}/{}?apikey={}".format(
        market, currency, locale, query, api_key
    )
    hotels = urllib2.urlopen(url).read()
    hotels = json.loads(hotels)

    return json.dumps(hotels)


# hotels have unique entity_id
def get_hotels_list(entity_id, checkin_date, checkout_date, guests, rooms):
    # create session
    api_key = get_api_key()
    url = "http://partners.api.skyscanner.net/apiservices/hotels/liveprices/v2/{}/{}/{}/{}/{}/{}/{}/{}?apiKey={}".format(
        market, currency, locale, entity_id, checkin_date, checkout_date, guests, rooms, api_key
    )
    hotels_list = urllib2.urlopen(url).read()
    # next_poll = "http://partners.api.skyscanner.net" + hotels_list.info().getheader('Location')
    # hotels_list = hotels_list.read()
    '''
    # polling session
    extended_hotels_list = [hotels_list]
    while hotels_list['status'] != "COMPLETE":
        hotels_list = urllib2.urlopen(next_poll)
        next_poll = "http://partners.api.skyscanner.net" + hotels_list.info().getheader('Location')
        hotels_list = hotels_list.read()
        hotels_list = json.loads(hotels_list)
        extended_hotels_list.append(hotels_list)
    return json.dumps(extended_hotels_list)'''
    return hotels_list
