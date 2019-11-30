#!/usr/bin/python

import cgi
import cgitb
import os

cgitb.enable()

print "Content-type:text/html"
print

form = cgi.FieldStorage()

# Set Upload Directory here.
UPLOAD_DIR = '/webtmp'

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
  fn = os.path.basename(fileitem.filename)
  uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(fileitem.filename))     
  with open(uploaded_file_path, 'wb') as f:
    f.write(fileitem.file.read())

  message = 'The file "' + fn + '" was uploaded successfully'
   
else:
  message = 'No file was uploaded'
   
print """
<html>
<body>
   <p>%s</p>
   <p>UPLOAD_DIR: %s</p>
   <p>uploaded_file_path: %s</p>
</body>
</html>
""" % (message, UPLOAD_DIR, uploaded_file_path)
