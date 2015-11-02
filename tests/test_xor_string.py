# !/usr/bin/env python

import unittest
from xor_string import xor_string

class EqualityTest(unittest.TestCase):
    def testEqual(self):
        ori = 'attack at dawn'
        enc = xor_string(ori, 's3cr3t')
        dec = xor_string(enc, 's3cr3t')
        self.failUnlessEqual(ori, dec)


if __name__ == '__main__':
    unittest.main()
