class EmptyException(Exception):
    pass

class LinkedQueue:
    """A queue implementation using an underlying singly linked list for storage"""

    class _Node:
        """A light weight object representing a single node of the list.
        A node maintains a reference to the element stored at this node and
        a reference to the next node."""

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise EmptyException("Queue is empty.")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyException("Queue is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
