#!/usr/bin/env python

import os

path = "/home/ubuntu/workspace/python-something/files"
max_files = 3

files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
         
print "Solo archivos"

i=-1
for file in files:
	i=i+1
	file_path = "/home/ubuntu/workspace/python-something/" + file
	if (i%max_files==0):
		dir = "/home/ubuntu/workspace/python-something/dir" + str(i)
		os.makedirs(dir)
		
	os.rename(file_path, dir)
	