#!/usr/bin/env python
import unittest
import sys
import my_lib

class TestMyLib(unittest.TestCase):

    def test_addthree(self):
        self.assertEqual(my_lib.add_three(0), 3)        
        self.assertEqual(my_lib.add_three(-3), 0)
        self.assertEqual(my_lib.add_three(-sys.maxint), -sys.maxint + 3)
       #self.assertEqual(my_lib.add_three(sys.maxint), sys.maxint + 3)

    def test_addfour(self):
        self.assertEqual(my_lib.add_four(0), 4)

    def test_addtwelve(self):
        self.assertEqual(my_lib.add_twelve(0), 12)
        return 


if __name__ == '__main__':
    unittest.main()
