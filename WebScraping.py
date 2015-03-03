#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import sys
import os
from HTMLParser import HTMLParser, HTMLParseError

class TestHTMLParser(HTMLParser):

    def __init__(self,tag):
        HTMLParser.__init__(self)
        self.tag = tag
        os.mkdir(self.tag)
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == self.tag:
            self.getImage(attrs["src"])

    def getImage(self, url):
        filename = self.tag + '/' + self.setName(url)
        r = urllib2.urlopen(url)
        f = open(filename, "wb")
        f.write(r.read())
        f.close()
        r.close()

    def setName(self, url):
        urlsp   = url.split('/')
        name    = urlsp[-1]
        return name

url = 'http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ipz549/'

parser = TestHTMLParser('img')
r = urllib2.urlopen(url)
htmldata = r.read()
parser.feed(htmldata)
parser.close()
