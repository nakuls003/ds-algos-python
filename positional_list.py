from doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """
    A sequential container of elements based on underlying doubly linked list
    """

    class Position:
        """
        An abstraction for the position of an element within the list
        """

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)

    def _validate(self, p):
        """
        validates position p and returns the node it encapsulates
        :param p:
        :return: node encapsulated by this position object
        """
        if not isinstance(p, self.Position):
            raise TypeError("p should be proper position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._next is None:
            raise ValueError("p is an invalid node.")
        return p._node

    def _make_position(self, node):
        """
        return the position wrapper for this node.
        return None if it is header or trailer sentinel node.
        :param node:
        :return: position object for this node
        """
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        oldval = original._element
        original._element = e
        return oldval
