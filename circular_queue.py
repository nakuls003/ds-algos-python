class EmptyException(Exception):
    pass


class CircularQueue:
    """A queue implementation using an underlying circularly linked list for storage"""

    class _Node:
        """A light weight object representing a single node of the list.
        A node maintains a reference to the element stored at this node and
        a reference to the next node."""

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise EmptyException("Queue is empty.")
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyException("Queue is empty.")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
