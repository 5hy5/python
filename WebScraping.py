#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.readlines()
for i in html:
    if "img" in i:
        print i
