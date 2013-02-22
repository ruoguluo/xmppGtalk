#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rluo
#
# Created:     20/01/2013
# Copyright:   (c) rluo 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import re
import sys
from pprint import pprint

def checkExchange(currency1, currency2):
    try:
        page = urllib2.urlopen("http://download.finance.yahoo.com/d/quotes.csv?s=%s%s=x&f=sl1d1t1ba&e=.csv"%(currency1,currency2))
        for line in page:
            print line
            (title, exchangeRate, day, time, bid, ask) = line.split(",")
            #print
            return {'exchangeRate':exchangeRate, 'day':day[1:-1], 'time':time[1:-1], 'bid':bid, 'ask':ask}

    except Exception, e:
        print "Error:\n%s" % e

if __name__ == '__main__':
    result = checkExchange("CAD", "CNY")
    print result['exchangeRate']