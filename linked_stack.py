class EmptyException(Exception):
    pass


class LinkedStack:
    """A stack implementation using an underlying singly linked list for storage"""

    class _Node:
        """A light weight object representing a single node of the list.
        A node maintains a reference to the element stored at this node and
        a reference to the next node."""

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise EmptyException("Stack is empty.")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise EmptyException("Stack is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
