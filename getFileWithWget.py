#!/usr/bin/env python
import subprocess
import os.path
import time
from os import listdir


#l1List = listdir("/cygdrive/c/Users/a/Desktop/US9_goods_batch/si2_env_20130627_1224")

outDir="/home/a/json"
for fileName in l1List:
	l1 = fileName.replace(".json","")
	filename = l1 + ".json"
	cmd = ['wget','-O', os.path.join(outDir, filename) ,'www.someurl.com/paht/xx.do?xxx=' + l1, ]
	print cmd
	subprocess.call(cmd)
	time.sleep(5) # sleeps for 5 secs
