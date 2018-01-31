"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    return("Hello")
    pass

def give_me_an_integer():
    """
    This function returns an integer value
    """
    return(1)
    pass

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    return(True)
    pass

def give_me_a_float():
    """
    This function returns a float value
    """
    return(1.2345)
    pass

def give_me_a_list():
    """
    This function returns a list
    """
    return(["one","two","three"])
    pass

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    return({"one" : "1", "two" : "2", "three" : "three"})
    pass

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    return(('one', 'two', 3, 4))
    pass

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    sumTen = 0

    for x in range(11):
    	sumTen += x
    return(sumTen)
    pass

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if ((number % 2) == 0):
    	return(True)
    else:
    	return(False)
    pass

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
    	return(True)
    else:
    	return(False)
    pass
