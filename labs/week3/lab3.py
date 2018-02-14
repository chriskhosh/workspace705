"""
lab3.py
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

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item ccheck_title(urrently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    inventory_dict = inventory

    for x in inventory_dict:
        inventory_dict.update({x : (inventory_dict.get(x) + 10)})

    return(inventory_dict)

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: tring that is the name of the inventory item
        value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    inventory_dict = {}

    for x in inventory:
        if inventory.get(x) != 0:
            inventory_dict.update({x : (inventory.get(x))})

    return(inventory_dict)

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
        key: string of students name
        value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    grades_dict = {}

    for x in grades:
        grades_dict[x] = (sum(grades[x]) / float(len(grades[x])))

    return(grades_dict)

if __name__ == '__main__':
    import doctest
    doctest.testmod()