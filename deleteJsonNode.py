#!/usr/bin/env python
import subprocess
from os import listdir
import sys

if len(sys.argv) < 3:
	sys.stderr.write("need directory path and node name to delete\n")

else:
	dir = sys.argv[1]
	flist = listdir(dir)
	nodeName = sys.argv[2]

	for f in flist:
		print "replacing... " + f
		path = dir + '/' + f
		after = ''

		before = '"' + nodeName + '":\s*"[^"]*",'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

		before = '"' + nodeName + '":\s*"[^"]*"'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

		before = '"' + nodeName + '":\s*null,'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

		before = '"' + nodeName + '":\s*null'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

