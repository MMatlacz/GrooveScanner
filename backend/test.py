import urllib2

from flask import json

import flyscanner
from flyscanner import return_grid

event = urllib2.urlopen('http://127.0.0.1:5000/matlaczm/app/event/210827955934810').read()
event = json.loads(event)
# print event

myairports = []
destairports = []
mycity = "warsaw"
mycountry = "Poland"

# print event['venue']['city']
airports = urllib2.urlopen('http://127.0.0.1:5000/matlaczm/app/airports/?q=' + event['venue']['city']).read()
airports = json.loads(airports)
for airport in airports['Places']:
    if str(airport['CountryName']).lower() == str(event['venue']['country']).lower() and str(
            airport['PlaceName']).lower() == str(event['venue']['city']).lower():
        destairports.append(airport)
airports = urllib2.urlopen('http://127.0.0.1:5000/matlaczm/app/airports/?q=' + mycity).read()
airports = json.loads(airports)
for airport in airports['Places']:
    if str(airport['CountryName']).lower() == str(mycountry).lower() and str(airport['PlaceName']).lower() == str(
            mycity).lower():
        myairports.append(airport)

# print "\n my {}".format(myairports)
# print "\n dest {}", format(destairports)
# print

connections = []
for start in myairports:
    for dest in destairports:
        connections.append(
            return_grid(flyscanner.market, flyscanner.currency, flyscanner.locale, start['PlaceId'], dest['PlaceId'],
                        '2016-08', '2016-09'))

for connect in connections:
    connect = json.loads(connect)
    carriers = connect['Carriers']
    dates = connect['Dates']
    currencies = connect['Currencies']
    places = connect['Places']

print connect
it = True
dates_table = []
for date in dates:
    dates_table.append(date)

departures = []

departures.append(dates_table[0])
dates_table.remove(departures[0])
for day in departures[0]:
    if day != None:
        print "\nday ",
        print json.dumps(day)
        for dep in dates_table[0]:
            if json.dumps(dep) != 'null':
                print "\t" + json.dumps(dep)
