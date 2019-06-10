"""
The Fibonacci sequence can be represented as a recurrence relation.
fn+1 = fn + fn-1, with f(0) = 1, and f(1) = 1
As such, we can calculate a close form representation, as taught in introductory
discrete structure courses. 

Approach: http://discrete.openmathbooks.org/dmoi2/sec_recurrence.html
"""

import math

def explicit_fibonacci(i):
     """
     time: O(1)
     space: O(1)
     """
     a = 1 / math.sqrt(5) * ((1 + math.sqrt(5)) / 2) ** i
     b = 1 / math.sqrt(5) * ((1 - math.sqrt(5)) / 2) ** i
     # Note: (1 + sqrt(5)) / 2 is the golden ratio!
     return round(a - b)
