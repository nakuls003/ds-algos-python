class EmptyException(Exception):
    pass


class ArrayDeque:
    """A deque implementation using an underlying list circularly"""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayDeque.DEFAULT_CAPACITY
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

    def back(self):
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def delete_front(self):
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def delete_back(self):
        if self.is_empty():
            raise EmptyException("Queue is empty!")
        last_index = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last_index]
        self._data[last_index] = None
        self._size -= 1
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def add_front(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_back(self, e):
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
