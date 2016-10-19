from linked_queue import LinkedQueue


class NotImplementedError(Exception):
    pass


class Tree:
    """
    An abstract base class representing a tree
    """

    class Position:
        """
        A class representing an abstraction for a location in a tree
        """

        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            return not(self == other)


    def root(self):
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height(p)

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadth_first_traversal(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def positions(self):
        return self.preorder()

    def __iter__(self):
        for p in self.positions():
            yield p.element()


