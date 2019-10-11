"""Queue implementation"""


class Queue:
    """Queue implementation"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        """Return whether the queue contains any items"""
        return not self._items

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Pop an item from the queue"""
        return self._items.pop()
