class _DoublyLinkedBase:
    """
    A class representing a doubly linked list. Any data structure implemented
    using an underlying doubly linked list will inherit from this class.
    """

    class _Node:
        """
        A lightweight object representing a node of the doubly linked list
        """

        def __init__(self, element, prev, nxt):
            self._element = element
            self._prev = prev
            self._next = nxt

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        ans = node._element
        node._element = node._prev = node._next = None
        return ans
