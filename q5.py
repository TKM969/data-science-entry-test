def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

import math
from numbers import Number

def check_divisibility(num, divisor):
    """
    Task 1
    - Check if num is divisible by divisor.
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    - Return -1 if either input is not numeric or if divisor is zero.
    """
    if not (isinstance(num, Number) and isinstance(divisor, Number)):
        return -1
    if divisor == 0:
        return -1

    # Fast path for integer inputs
    if isinstance(num, int) and isinstance(divisor, int):
        return num % divisor == 0

    # For floats or mixed numeric types, check quotient is (near) integer
    quotient = num / divisor
    return math.isclose(quotient, round(quotient), rel_tol=0.0, abs_tol=1e-9)

print(check_divisibility(10, 2))      # True
print(check_divisibility(7, 3))       # False
print(check_divisibility(7.5, 2.5))   # True
print(check_divisibility(7.5, 2))     # False
print(check_divisibility("a", 2))     # -1
print(check_divisibility(5, 0))       # -1


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

... def check_divisibility(num, divisor):
...     """
...     Task 1
...     - Check if num is divisible by divisor.
...     - Both num and divisor must be numeric.
...     - Return True if num is divisible by divisor, False otherwise.
...     - Return -1 if either input is not numeric or if divisor is zero.
...     """
...     if not (isinstance(num, Number) and isinstance(divisor, Number)):
...         return -1
...     if divisor == 0:
...         return -1
...
...     # Fast path for integer inputs
...     if isinstance(num, int) and isinstance(divisor, int):
...         return num % divisor == 0
...
...     # For floats or mixed numeric types, check quotient is (near) integer
...     quotient = num / divisor
...     return math.isclose(quotient, round(quotient), rel_tol=0.0, abs_tol=1e-9)
... print(check_divisibility(10, 2))      # True
... print(check_divisibility(7, 3))       # False
... print(check_divisibility(7.5, 2.5))   # True
... print(check_divisibility(7.5, 2))     # False
... print(check_divisibility("a", 2))     # -1
... print(check_divisibility(5, 0))       # -1
...
True
False
True
False
-1
-1