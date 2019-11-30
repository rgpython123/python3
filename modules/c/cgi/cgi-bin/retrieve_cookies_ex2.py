#!/usr/bin/env python 

# enable debugging
import cgi
import cgitb
import os

cgitb.enable()

print "Content-type:text/html"
print
if 'HTTP_COOKIE' in os.environ:
  for cookie in os.environ['HTTP_COOKIE'].split(';'):
    (key, value ) = cookie.strip().split('=')
    if key == "UserID":
       user_id = value
    elif key == "Password":
       password = value
else:
  print "HTTP_COOKIE not set!"

print "<H2>%s</H2>" % os.environ['HTTP_COOKIE']
print "<H2>User ID  = %s</H2>" % user_id
print "<H2>Password = %s</H2>" % password
