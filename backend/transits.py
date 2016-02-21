import urllib2

import itertools
from flask import json

import flyscanner
from flyscanner import return_grid


def get_connections(event_city, event_country, start_city, start_country, out_time, in_time):
    outairports = []
    destairports = []
    print event_city, event_country, start_city, start_country, out_time, in_time
    airports = json.loads(flyscanner.get_airports(event_city))
    for airport in airports['Places']:
        if str(airport['CountryName']).lower() == str(event_country).lower() and str(
                airport['PlaceName']).lower() == str(event_city).lower():
            destairports.append(airport)
    airports = json.loads(flyscanner.get_airports(start_city))
    print "airports2"
    for airport in airports['Places']:
        if str(airport['CountryName']).lower() == str(start_country).lower() and str(
                airport['PlaceName']).lower() == str(start_city).lower():
            outairports.append(airport)

    connections = []
    for start in outairports:
        for dest in destairports:
            connections.append(
                return_grid(flyscanner.market, flyscanner.currency, flyscanner.locale, start['PlaceId'],
                            dest['PlaceId'],
                            out_time, in_time))

    for conn in connections:
        conn = json.loads(conn)
        carriers = conn['Carriers']
        dates = conn['Dates']
        currencies = conn['Currencies']
        places = conn['Places']
    output = {'flights': {}}
    i = 0
    for inbound in dates[1:]:
        for d1, d2 in itertools.izip(dates[0], inbound[1:]):
            if d2 is None or d1 is None or inbound[0] is None:
                continue
            i += 1
            output['flights'][i] = {"Out": d1['DateString'], "In": inbound[0]['DateString'], "Price": d2['MinPrice'],
                                    "QuoteDateTime": d2['QuoteDateTime']}
            print d1
            print inbound[0]
            print d2
            print
    output['places'] = places
    return json.dumps(output)

# result = get_connections("Barcelona", "Spain", "Brussels", "Belgium", "2016-08", "2016-08")
# print result
