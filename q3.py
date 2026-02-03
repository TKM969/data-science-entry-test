def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


>>> def update_dictionary(dct, key, value):
...     """
...     Task 1
...     - Create a function that updates a dictionary (dct) with a new key-value pair.
...     - If the key already exists in dct, print the original value, then update its value.
...     - Return the updated dictionary.
...     """
...     if not isinstance(dct, dict):
...         raise TypeError("dct must be a dictionary")
...     if key in dct:
...         print(dct[key])
...     dct[key] = value
...     return dct
... my_dict = {"a": 1, "b": 2}
...
... # Key exists: prints original value 2, updates "b"
... updated = update_dictionary(my_dict, "b", 5)
... print(updated)  # {'a': 1, 'b': 5}
...
... # Key does not exist: no print, adds new key "c"
... updated = update_dictionary(my_dict, "c", 10)
... print(updated)  # {'a': 1, 'b': 5, 'c': 10}
...
2
{'a': 1, 'b': 5}
{'a': 1, 'b': 5, 'c': 10}
>>>

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

>>> def update_dictionary(dct, key, value):
...     """
...     Create a function that updates a dictionary (dct) with a new key-value pair.
...     If the key already exists in dct, print the original value, then update its value.
...     Return the updated dictionary.
...     """
...     if not isinstance(dct, dict):
...         raise TypeError("dct must be a dictionary")
...     if key in dct:
...         print(dct[key])
...     dct[key] = value
...     return dct
...
... # Task 2 invocations
... result1 = update_dictionary({}, "name", "Alice")
... print("result1:", result1)
...
... result2 = update_dictionary({"age": 25}, "age", 26)
... print("result2:", result2)
...
result1: {'name': 'Alice'}
25
result2: {'age': 26}
>>>
