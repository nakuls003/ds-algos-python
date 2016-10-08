from positional_list import PositionalList


class FavouritesList:
    """
    An abstract data type storing a sequence of elements in order of their access count
    i.e. the most popular/most accessed elements occur first. Uses a doubly linked list as underlying storage
    """

    class _Item:
        """
        a composite object containing an element of the favourites list as well as its access count
        """
        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        """
        find the position in the list where e is stored or return None
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """
        consider moving element at position p further ahead in the sequence to preserve the invariant i.e.
        elements of the sequence must be stored in non-increasing order.
        """
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def access(self, e):
        """
        access element e and increase its access count.
        """
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """
        return an iteration of the top k most accessed elements of the list
        """
        if not 1 <= k <= len(self):
            raise ValueError("Invalid value of k.")
        walk = self._data.first()
        for i in range(k):
            yield walk.element()._value
            walk = self._data.after(walk)
