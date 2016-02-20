import urllib2

print urllib2.urlopen('http://freegeoip.net/json/').read()

import locale
lang = list(locale.getlocale('EN'))
print lang