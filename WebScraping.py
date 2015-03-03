#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import sys
import os
import errno
from HTMLParser import HTMLParser, HTMLParseError

class TestHTMLParser(HTMLParser):

    def __init__(self,tag):
        HTMLParser.__init__(self)
        self.tag = tag
        try:
            os.mkdir(self.tag)
        except OSError, e:
            if e.errno != errno.EEXIST:
                raise e
            pass

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == self.tag:
            self.getImage(attrs["src"])

    def getImage(self, url):
        filename = self.tag + '/' + self.setName(url)
        response = urllib2.urlopen(url)
        newfile  = open(filename, "wb")
        newfile.write(response.read())
        response.close()
        newfile.close()

    def setName(self, url):
        urlist  = url.split('/')
        name    = urlist[-1]
        return name

url = ''

parser = TestHTMLParser('img')
r = urllib2.urlopen(url)
htmldata = r.read()
parser.feed(htmldata)
parser.close()
