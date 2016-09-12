# based on http://docs.python-guide.org/en/latest/writing/tests/

# To install py.test, enter this command in Command-line / Terminal:
# pip install pytest

# To run the test using py.test, enter this command in Command-line / Terminal:
# py.test ut.py -v

def myfun(x):
    return x**2

# Note: test functions must start with the un-capitalized characters "test"

def test_this():
    assert myfun(3) == 9

def test_that():
    myvar = myfun(0)
    assert myfun(1) == 1
    assert myfun(2) == 4
    assert myvar == 0
    assert myfun(3) == 5 # should cause error