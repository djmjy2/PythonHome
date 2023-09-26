# import unittest
import test_function

# class MyTest(unittest.TestCase) :
#     def test_sum(self):
#         self.assertEqual(test_function.sum(2,5),7)
    
#     def test_multiple(self):
#         self.assertEqual(test_function.multiple(2,5),9)
#### python -m unittest test.py ####

def test_sum() :
    assert test_function.sum(2,5) == 7 
    assert test_function.sum(2.1,6.3) == 8.4
    
def test_multiple () :
    assert test_function.multiple(2,5) == 10
    assert test_function.multiple(2.2,3.0) == 6.6
#### pytest test.py #####