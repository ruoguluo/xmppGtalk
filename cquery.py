import urllib2
import re
import sys
from pprint import pprint

def cquery(url):
    try:
        print "opening",url         
        pageReturn = urllib2.urlopen(url)
        return pageReturn.readline() 
    except Exception, e:
        print "Error:\n%s" % e

if __name__ == '__main__':
    result = cquery("http://cquery.com/api/fetch/?api_key=cq51251ee9c72ad&source_url=http://www.6park.com&css_selector=div%23parknews&data_type=text&response_format=raw&checkField=tomato")
    print "result",result
