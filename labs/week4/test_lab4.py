"""
Lab 4 test file
Christian Khoshatefeh
2/13/18
"""
import unittest

class Lab4Test(unittest.TestCase):

    def test_squared(self):
        """
        Tests lab4.squared_nums()
        """
        func = lab4.squared_nums
        case1 = [1, 2, 3]
        expected1 = [1, 4, 9]
        self.assertEqual(func(case1), expected1)

    def test_check_title(self):
        """
        Tests lab4.check_title()
        """
        func = lab4.check_title
        case1 = ['Hello there','Hello There','Hello there 3']
        expected1 = ['Hello There']
        self.assertEqual(func(case1), expected1)


if __name__ == '__main__':
    try:
        import lab4
        print("lab4.py module found, testing...")
        unittest.main()
    except ImportError:
        print("Missing lab4.py module")