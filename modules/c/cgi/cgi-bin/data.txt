#!/usr/bin/python

# HTTP Header
print "Content-Type:application/octet-stream; name = \"FileName\"\r\n";

# Actual File Content will go here.
with open("/webtmp/data.txt", "rb") as f:
  data = f.read()

print(data)

# NOTE: Change the name of this file to data.txt.
#       This code will place the contents of "/webtmp/data.txt" into a
#       downloaded file to the user with the name of this file. 
