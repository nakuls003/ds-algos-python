from positional_list import PositionalList


class EmptyException(Exception):
    pass


class PriorityQueueBase:
    """
    An abstract base class for different implementations of priority queue
    """

    class _Item:
        """
        A composite object storing an element and its priority
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    A priority queue class storing elements in arbitrary order
    """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        if self.is_empty():
            raise EmptyException("Priority Queue is empty.")
        curr_min = self._data.first()
        walk = self._data.after(curr_min)
        while walk is not None:
            if walk.element() < curr_min.element():
                curr_min = walk
            walk = self._data.after(walk)
        return curr_min

    def min(self):
        p = self._find_min()
        return (p.element()._key, p.element()._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

    def add(self, k, v):
        self._data.add_last(self._Item(k, v))


class SortedPriorityQueue(PriorityQueueBase):
    """
    A priority queue class storing elements sorted according to priority
    """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def min(self):
        if self.is_empty():
            raise EmptyException('Priority queue is empty.')
        p = self._data.first()
        return (p.element()._key, p.element()._value)

    def remove_min(self):
        if self.is_empty():
            raise EmptyException('Priority queue is empty.')
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)

    def add(self, k, v):
        newest = self._Item(k, v)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
