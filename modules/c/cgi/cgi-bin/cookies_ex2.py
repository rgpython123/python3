#!/usr/bin/env python 

# enable debugging
import cgitb
cgitb.enable()

print "Set-Cookie:UserID = XYZ;"
print "Set-Cookie:Password = XYZ123;"
print "Set-Cookie:Expires = Tuesday, 25-Dec-2018 23:12:40 GMT;"
print "Content-type:text/html"
print
print "Hello, World! ... from Python's CGI with cookies."
