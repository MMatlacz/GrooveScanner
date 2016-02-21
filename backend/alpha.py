import urllib
import urllib2
from xml.etree import ElementTree as etree
#pod

class wolfram(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}

    ip = "Barcelona International Airport"

    def get_airport_details(self, name):
        #details = urllib2.urlopen("http://api.wolframalpha.com/v2/query?input=" + name + "&appid=GK3LPL-YW5RJ662W4").read()
        ip = name
        xml = self._get_xml(ip)
        result_dics = self._xmlparser(xml)

        print 'Available Titles', '\n'
        titles = dict.keys(result_dics)
        for ele in titles : print '\t' + ele
        print '\n'
        print result_dics

    def _get_xml(self, ip):
            url_params = {'input':ip, 'appid':self.appid}
            data = urllib.urlencode(url_params)
            print data
            req = urllib2.Request(self.base_url, data, self.headers)
            xml = urllib2.urlopen(req).read()
            return xml

    def _xmlparser(self, xml):
             data_dics = {}
             tree = etree.fromstring(xml)
             #retrieving every tag with label 'plaintext'
             for e in tree.findall('pod'):
                 for item in [ef for ef in list(e) if ef.tag=='subpod']:
                     for it in [i for i in list(item) if i.tag=='plaintext']:
                         if it.tag=='plaintext':
                             data_dics[e.get('title')] = it.text
             return data_dics

appid = 'GK3LPL-YW5RJ662W4'
w = wolfram(appid)
w.get_airport_details("BHX")