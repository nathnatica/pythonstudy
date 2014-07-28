#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys
import datetime

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
        print 'Usage: python %s date(yyyy/mm/dd)' % argvs[0]
        sys.exit(1)

if (argvs[1] == "-1"):
        d = datetime.date.today()
        t = datetime.timedelta(days = 2)
        target_day = (d - t).strftime("%Y/%m/%d")
else:
        target_day = argvs[1]

url = 'https://www.google.com'
username = 'user'
password = 'pass'

print url

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, password)

opener = urllib2.build_opener(urllib2.HTTPSHandler(), urllib2.HTTPBasicAuthHandler(password_mgr))
urllib2.install_opener(opener)

req = urllib2.Request(url)
try:
        res = urllib2.urlopen(req).read()
except urllib2.URLError, e:
        print e
        sys.exit(1)

f = open('output.txt', 'w')
f.write(res)
f.close()
