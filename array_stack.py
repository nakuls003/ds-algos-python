class EmptyException(Exception):
    pass


class ArrayStack:
    """A stack implementation using an underlying list for storage"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise EmptyException("Stack is empty.")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyException("Stack is empty.")
        return self._data[-1]


def is_valid_expression(expr):
    """Validates an arithmetic expression by matching delimiters"""
    S = ArrayStack()
    lefty = '({['
    righty = ')}]'
    for ch in expr:
        if ch in lefty:
            S.push(ch)
        elif ch in righty:
            if S.is_empty():
                return False
            if righty.index(ch) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def is_valid_html(raw):
    """validates HTML text by matching opening and closing tags"""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()
