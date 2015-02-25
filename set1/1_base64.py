import sys
import base64
import binascii

words = iter(sys.argv)
next(words)

for w in words:
  x = binascii.unhexlify(w)
  x = base64.b64encode(x)
  print x
