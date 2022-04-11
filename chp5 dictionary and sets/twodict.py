# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}  

z
{'c': 4, 'a': 1, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
#