import bz2
import os

data = open('data.txt', 'r').read() * 1024
print 'Input contains %d bytes' % len(data)

for i in xrange(1, 10):
    filename = 'data.txt-compress-level-%s.bz2' % i
    output = bz2.BZ2File(filename, 'wb', compresslevel=i)
    try:
        output.write(data)
    finally:
        output.close()
    os.system('cksum %s' % filename)
