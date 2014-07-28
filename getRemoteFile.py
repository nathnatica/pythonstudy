#!/usr/bin/python

import sys
import subprocess

argvs = sys.argv
argc = len(argvs)

if (argc != 3) :
        print 'Usage: getRemoteFile.py (country) (site)'
	print '       country [jp], site [pcfront|mbfront|pctshop|mbtshop]'
        sys.exit(1)


hostDict = {'pcfront':'127.0.0.1', 'mbfront':'127.0.0.1','pctshop':'127.0.0.127.0.0.1','mbtshop':'127.0.0.1'}
try:
	host = hostDict[argvs[2]]
except:
	print 'input valid site [pcfront|mbfront|pctshop|mbtshop]'
	sys.exit(1)


pathDict = {'jppcfront':'/path1/', \
		'jpmbfront':'/path2/', \
		'jppctshop':'/path3/', \
		'jpmbtshop':'/path4/'}
try:
	path = pathDict[argvs[1] + argvs[2]]
except:
	print 'input valid country [jp], site [pcfront|mbfront|pctshop|mbtshop]'
	sys.exit(1)


host = 'tomcat@' + host
catFile = 'front_ja_JP.properties'
ssh = subprocess.Popen(['ssh', host, 'cat', path + catFile], stdout=subprocess.PIPE)


f = open('/cygdrive/c/Users/output/Desktop/' + host + '_' + argvs[2] + '_' + catFile, 'w')

for line in ssh.stdout.readlines():
	f.write(line)
	print line,

f.close()
