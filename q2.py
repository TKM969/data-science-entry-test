def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return

>>> def find_and_replace(lst, find_val, replace_val):
...     """
...     Task 1
...     - Search for all occurrences of find_val in lst and replace them with replace_val.
...     - lst must be a list.
...     - Return the modified list. Return -1 if lst is not a list.
...     """
...     if not isinstance(lst, list):
...         return -1
...     for i, v in enumerate(lst):
...         if v == find_val:
...             lst[i] = replace_val
...     return lst
... print(find_and_replace([1, 2, 3, 2, 4], 2, 99))   # [1, 99, 3, 99, 4]
... print(find_and_replace("not a list", 2, 99))      # -1
...
[1, 99, 3, 99, 4]
-1



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


>>> # Task Invoke find_and_replace
...
... **Scenarios**
... - `find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)`
... - `find_and_replace(["apple", "banana", "apple"], "apple", "orange")`
...
... **Behavior**
... - If `lst` is not a list → function returns `-1`.
... - Otherwise all occurrences of `find_val` are replaced with `replace_val` and the modified list is returned.
... def find_and_replace(lst, find_val, replace_val):
...     """
...     Search for all occurrences of find_val in lst and replace them with replace_val.
...     lst must be a list. Return -1 if lst is not a list. Otherwise return the modified list.
...     """
...     if not isinstance(lst, list):
...         return -1
...     for i, v in enumerate(lst):
...         if v == find_val:
...             lst[i] = replace_val
...     return lst
...
... # Invocations for the requested scenarios
... result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
... print("result1:", result1)
...
... result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
... print("result2:", result2)
...
