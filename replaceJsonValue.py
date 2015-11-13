#!/usr/bin/env python
import subprocess
from os import listdir
import sys

if len(sys.argv) < 3:
	sys.stderr.write("need directory path and node name to replace value\n")
	
else:
	dir=sys.argv[1]
	flist = listdir(dir)
	nodeName = sys.argv[2]

	for f in flist:
		print "replacing... " + f
		path = dir + '/' + f
        before = '"' + nodeName + '":\s*"[^"]*"'
        after = '"' + nodeName + '":"anything"'
		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])

#		before = '"goods_sub_image_list":"[^"]*",' # sed is not supporting non-greedy regex, use [^] pattern
#		subprocess.call(['sed','-i','s/' + before + '/' + after + '/g', path])




