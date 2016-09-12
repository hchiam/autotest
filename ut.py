# based on http://docs.python-guide.org/en/latest/writing/tests/

# To run the test using unittest, enter this command in Command-line / Terminal:
# python ut.py -v

import unittest

def myfun(x):
    return x**2

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(myfun(3),9)

if __name__ == "__main__":
    unittest.main()