class EmptyException(Exception):
    pass


class ArrayQueue:
    """A queue implementation using an underlying list circularly"""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
