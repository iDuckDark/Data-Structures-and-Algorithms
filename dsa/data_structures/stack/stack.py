"""
Stack implementation

References:
- https://bradfieldcs.com/algos/stacks/implementation/
"""


class Stack:
    """Stack"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        """Return whether the stack contains any items"""
        return not self._items

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Pop an item from the stack"""
        return self._items.pop()
