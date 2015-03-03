#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
url = ''
tag = ''
response = urllib2.urlopen(url)
html = response.readlines()
for i in html:
    if tag in i:
        print i
