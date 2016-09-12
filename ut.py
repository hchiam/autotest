# command in Command-line / Terminal to run the test:
# python ut.py

# or for more detail:
# python ut.py -v

import unittest

def myfun(x):
    return x**2

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(myfun(3),9)

if __name__ == "__main__":
    unittest.main()