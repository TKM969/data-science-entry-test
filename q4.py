def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return

>>> def string_reverse(s):
...     """
...     Task 1
...     - Reverse a given string s.
...     - s must be a string.
...     - Return -1 if s is not a string.
...     - Return the reversed string otherwise.
...     """
...     if not isinstance(s, str):
...         return -1
...     return s[::-1]
... print(string_reverse("hello"))    # "olleh"
... print(string_reverse(""))         # ""
... print(string_reverse(123))        # -1
...
olleh

-1


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

def string_reverse(s):
    """
    Reverse a given string s.
    s must be a string.
    Return -1 if s is not a string; otherwise return the reversed string.
    """

>>> def string_reverse(s):
...     """
...     Reverse a given string s.
...     s must be a string.
...     Return -1 if s is not a string; otherwise return the reversed string.
...     """
...     if not isinstance(s, str):
...         return -1
...     return s[::-1]
... print(string_reverse("hello"))    # "olleh"
... print(string_reverse(""))         # ""
... print(string_reverse(123))        # -1
...
olleh

-1
