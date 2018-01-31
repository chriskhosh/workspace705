"""
lab2.py
Christian Khoshatefeh
1/30/18
"""

def squared_nums(num_list):
    """
    Squares numbers in the num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    squared_list = []

    for num in num_list:
        sq_num = num * num
        squared_list.append(sq_num)

    return(squared_list)

def check_title(title_list):
    """Removes strins in the title list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    list_title = []

    for x in title_list:
        if x == x.title():
            list_title.append(x)

    return(list_title)
