"""
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0. For the sake of comparison,
non-existing elements are considered to be infinite. The interesting
property of a heap is that a[0] is always its smallest element.

Links:
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    https://github.com/python/cpython/blob/master/Lib/heapq.py
    https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
"""


class MinHeap:
    """Implementation of min heap"""

    def __init__(self, arr=None):
        if arr:
            # Transform bottom-up.  The largest index there's any point to looking at
            # is the largest with a child index in-range, so must have 2*i + 1 < n,
            # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
            # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
            # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
            # O(n) time, in place
            self.heap = arr
            for i in reversed(range(len(self) // 2)):
                self._siftup(i)

        self.heap = []

    def __len__(self):
        return len(self.heap)

    def _siftdown(self, startpos, pos):
        """
        'heap' is a heap at all indices >= startpos, except possibly for
        pos. pos is the index of a leaf with a possibly out-of-order value.
        Restore the heap invariant.
        """
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) // 2
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2 * pos + 1  # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)

    def push(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.heap.append(item)
        self._siftdown(0, len(self.heap) - 1)

    def pop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()  # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup(0)
            return returnitem
        return lastelt


def test():
    """run test cases"""
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    assert heap.heap == [3, 5]
    assert heap.pop() == 3
    assert heap.heap == [5]


if __name__ == "__main__":
    test()
