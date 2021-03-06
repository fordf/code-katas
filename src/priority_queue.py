"""Implementation of Priority Queue."""
from bin_heap import BinaryHeap


class PriorityQueue(object):
    """Priority list queue."""

    def __init__(self, iterable=None):
        """Construct priority queue."""
        self._heap = BinaryHeap()
        self._count = 0
        if iterable:
            try:
                for item in iterable:
                    self.insert(item)
            except TypeError:
                raise TypeError("Optional argument of priority queue must be iterable.")

    def insert(self, data, priority=0):
        """Add item to queue given data and item's priority."""
        self._heap.push((priority, self._count, data))
        self._count = 1

    def pop(self):
        """Remove and return first inserted item of highest priority."""
        try:
            return self._reformat(self._heap.pop())
            self._count -= 1
        except IndexError:
            raise IndexError('Cannot pop from empty priority queue.')

    def peek(self):
        """Peek at the highest priority tuple."""
        return self._reformat(self._heap._list[0])

    def pop_all(self):
        """Remove and return all inserted items as a list in order of priority."""
        res = []
        while True:
            try:
                res.append(self.pop()[0])
            except IndexError:
                break
        return res

    @staticmethod
    def _reformat(item):
        """Reformat tuple to way it was pushed."""
        return tuple([item[2], item[0]])
