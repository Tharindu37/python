# This is a comments

"This is another awesome string"

"""
This is a comments
This is another awesome string
"""

def my_fun(x:int=None, y:int=None) -> int: # list, dict, int
    """
    This function does something
    @param x: first number
    @param y: second number
    @returns: multiplication of x and y
    """
    return x*y
# BUG, FIXME
# TODO: Change this some other time 
a = my_fun("text", 5)
print(a)