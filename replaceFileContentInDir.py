#!/usr/bin/env python
import subprocess
from os import listdir
import sys

if len(sys.argv) < 2:
	sys.stderr.write("need directory path\n")
	
else:
	dir=sys.argv[1]
	flist = listdir(dir)

	for f in flist:
		print "replacing... " + f
		path = dir + '/' + f
		before = '"timestamp":\s*"[0-9]*"'
		after = '"timestamp":"anytime"'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

#		before = '"goods_sub_image_list":"[^"]*",' # sed is not supporting non-greedy regex, use [^] pattern
#		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])
#		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])




