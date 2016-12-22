#!/usr/bin/python3
import time;  # This is required to include time module.

print (time.localtime())

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)