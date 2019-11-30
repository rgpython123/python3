import bz2
import os
import sys

file = sys.argv[1]
bz2_compress_level = 9

with open(file, 'r') as f:
  data = f.read()
  print 'Input contains %d bytes' % len(data)

filename = '%s.bz2' % (file)
output = bz2.BZ2File(filename, 'wb', compresslevel=bz2_compress_level)
try:
    print 'Creating: %s' % filename
    output.write(data)
finally:
    output.close()
os.system('cksum %s' % filename)
