from doubly_linked_base import _DoublyLinkedBase


class EmptyException(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):
    """
    A deque implementation using an underlying doubly linked list for storage
    """

    def front(self):
        if self.is_empty():
            raise EmptyException("Deque is empty")
        return self._header._next._element

    def back(self):
        if self.is_empty():
            raise EmptyException("Deque is empty")
        return self._trailer._prev._element

    def add_front(self, e):
        self._insert_between(e, self._header, self._header._next)

    def add_back(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def remove_front(self):
        if self.is_empty():
            raise EmptyException("Deque is empty")
        return self._delete_node(self._header._next)

    def remove_back(self):
        if self.is_empty():
            raise EmptyException("Deque is empty")
        return self._delete_node(self._trailer._prev)
