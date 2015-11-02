#!/usr/bin/env python
from itertools import cycle, izip

def xor_string(message, key):
    cyphered = ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
    # print('%s ^ %s = %s' % (message, key, cyphered))
    return cyphered

if __name__ == '__main__':
    enc = xor_string('attack at dawn', 's3cr3t')
    dec = xor_string(enc, 's3cr3t')
    print(enc)
    print(dec)
