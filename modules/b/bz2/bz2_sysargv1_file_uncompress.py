import bz2
import os
import sys

file = sys.argv[1]

base_file, ext = os.path.splitext(file)

input_file = bz2.BZ2File(file, 'rb')

try:
  with open(base_file, 'wb') as output_file:
    print('Uncompressing "%s" to "%s"' % (file, base_file))
    output_file.write(input_file.read())
except Exception as e:
  print('Exception: %s' % e)
