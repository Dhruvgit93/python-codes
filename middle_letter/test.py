import unittest
from solution import find_middle_letters

class test(unittest.TestCase):
    def test_odd(self):
        result=find_middle_letters("hello")
        self.assertEqual(result,"l")
    def test_even(self):
        result=find_middle_letters("helloo")
        self.assertEqual(result,"ll")
    def test_empty(self):
        result=find_middle_letters("")
        self.assertEqual(result,"")


if __name__=="__main__":
    unittest.main()