def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return

>>> from numbers import Number
...
... def swap(x, y):
...     """
...     Swap x and y using only x and y as variables.
...     Return -1 if either is not numeric; otherwise print swapped values.
...     """
...     if not (isinstance(x, Number) and isinstance(y, Number)):
...         return -1
...     x, y = y, x
...     print(x, y)
... # Example 1: both numeric
... result = swap(3, 7)   # prints: 7 3 ; result is None
... print("return:", result)
...
... # Example 2: one non-numeric
... result = swap("a", 1) # returns -1
... print("return:", result)
...
7 3
return: None
return: -1
>>>




# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

>>> # Task 2 Invoke swap
...
... **Scenarios**
... - Invoke `swap("Apple", 10)`
... - Invoke `swap(9, 17)`
...
... **Mathematical formula**
... $$
... x',\,y' = y,\,x
... $$
...
... **Behavior**
... - If either argument is non‑numeric → function returns `-1`.
... - If both are numeric → function prints swapped values.
>>> from numbers import Number
...
... def swap(x, y):
...     """
...     Swap x and y using only x and y as variables.
...     Return -1 if either is not numeric; otherwise print swapped values.
...     """
...     if not (isinstance(x, Number) and isinstance(y, Number)):
...         return -1
...     x, y = y, x
...     print(x, y)
...
... # Invocations for Task 2
... result1 = swap("Apple", 10)
... print("return:", result1)
...
... result2 = swap(9, 17)
... print("return:", result2)
...
return: -1
    
