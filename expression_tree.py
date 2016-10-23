from linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """
    A binary tree class for representing and evaluating an arithmetic expression
    """

    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string.')
        self._add_root(token)
        if left is not None:
            if token not in '+-*/':
                raise ValueError('Token must be an operator.')
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, results):
        if self.is_leaf(p):
            results.append(str(p.element()))
        else:
            results.append('(')
            self._parenthesize_recur(self.left(p), results)
            results.append(str(p.element()))
            self._parenthesize_recur(self.right(p), results)
            results.append(')')

    def evaluate(self):
        return self._evaluate(self.root())

    def _evaluate(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = str(p.element())
            left_val = self._evaluate(self.left(p))
            right_val = self._evaluate(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            else:
                return left_val / right_val


def build_expression_tree(tokens):
    """
    build an expression tree by parsing tokenized input from user
    """
    s = []
    for t in tokens:
        if t in '+-*/':
            s.append(t)
        elif t.isdigit():
            s.append(ExpressionTree(t))
        elif t == ')':
            right = s.pop()
            op = s.pop()
            left = s.pop()
            s.append(ExpressionTree(op, left, right))

    return s.pop()
