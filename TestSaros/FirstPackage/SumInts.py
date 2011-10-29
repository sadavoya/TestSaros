'''
Created on Oct 23, 2011

@author: XPMUser
'''
def sum_ints(x):
    if (isinstance(x, int)):
        return x
    elif (isinstance(x, list)):
        if (len(x) > 1):
            return sum_ints(x[0]) + sum_ints(x[1:])
        elif (len(x) == 1):
            return sum_ints(x[0])
        else:
            return 0
    else:
        return 0

def test_sum_ints():
    if (assert1(sum_ints(3), 3, 1) +
        assert1(sum_ints('a'), 0, 2) +
        assert1(sum_ints('3'), 0, 3) +
        assert1(sum_ints(3.0), 0, 4) +
        assert1(sum_ints([3]), 3, 5) +
        assert1(sum_ints([]), 0, 6) +
        assert1(sum_ints([[[[3]]]]), 3, 7) +
        assert1(sum_ints([[2], 3, [[4, 5, 'a']]]), 14, 8) +
        assert1(sum_ints({1: 2, 3: 4}), 0, 9) +
        assert1(sum_ints((1, 2, 3, 4)), 0, 10) == 0):
            print "no errors"
        

def test_assert1():
    assert1(1, 0, "Should be printed")
    assert1(0, 0, "Should not be printed")


def assert1(actual, expected, message):
        if expected != actual:
            print message.__str__() + "; expected: " + expected.__str__() + "; actual: " + actual.__str__()
            return 1
        else: 
            return 0

test_sum_ints()