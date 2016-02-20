import urllib2
import pycountry
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

def get_hotels_ids(query): #query is city name
    api_key = get_api_key()
    url = "http://partners.api.skyscanner.net/apiservices/hotels/autosuggest/v2/{}/{}/{}/{}?apikey={}".format(
        market, currency, locale, query, api_key
    )
    hotels = urllib2.urlopen(url).read()
    hotels = json.loads(hotels)

    return json.dumps(hotels)

# hotels have got unique entity_id
def get_hotels_list(entity_id, checkin_date, checkout_date, guests, rooms):
    #create session
    api_key = get_api_key()
    url = "http://partners.api.skyscanner.net/apiservices/hotels/liveprices/v2/{}/{}/{}/{}/{}/{}/{}/{}?apiKey={}".format(
        market, currency, locale, entity_id, checkin_date, checkout_date, guests, rooms, api_key )
    hotels_list = urllib2.urlopen(url)
    next_poll = hotels_list.info().getheader('Location')
    hotels_list = hotels_list.read()
    hotels_list = json.loads(hotels_list)

    print "-----"
    print hotels_list
    #polling session
    extended_hotels_list = [hotels_list]
    while hotels_list['status'] != "COMPLETE":
        hotels_list = urllib2.urlopen(next_poll)
        next_poll = hotels_list.info().getheader('Location')
        hotels_list = hotels_list.read()
        hotels_list = json.loads(hotels_list)
        extended_hotels_list.append(hotels_list)
    print extended_hotels_list
    return extended_hotels_list


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
