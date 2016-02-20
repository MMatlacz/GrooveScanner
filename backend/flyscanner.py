import urllib2
from flask import json


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

market = "UK"
currency = "EUR"
locale = "en-GB"

def get_airports(query):
    api_key = get_api_key()
    url = 'http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/{}/{}/{}/?query={}&apiKey={}'.format(
        market, currency, locale, query, api_key
    )
    currencies = urllib2.urlopen(url).read()
    currencies = json.loads(currencies)

    return json.dumps(currencies)


#print get_currencies()
#countries = json.loads(get_markets('en-GB'))['Countries']
#print countries
#print "\n"
'''
country = ''
for c in countries:
    if c['Name'] == 'Poland':
        country = c['Code']
        '''
#print country
#print get_airports("Barcelona")
#print get_locales()
#print return_grid(market, currency, locale, 'WARS-sky', 'BARC-sky', '2016-08', '2016-09' )
