import math


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.gradient = 0
        self.backward = lambda: None

    def int_to_node(self, other):
        return other if isinstance(other, Node) else Node(other)

    def __add__(self, other):
        other = self.int_to_node(other)

        res = Node(self.val + other.val)

        def _backward():
            self.gradient += res.gradient
            other.gradient += res.gradient

        res.backward = _backward

        return res

    def __pow__(self, other):
        other = self.int_to_node(other)

        res = Node(self.val ** other.val)

        def _backward():
            self.gradient += (other * self.val**(other-1)) * res.gradient

        res.backward = _backward

        return res

    def __mul__(self, other):
        other = self.int_to_node(other)

        res = Node(self.val * other.val)

        def _backward():
            self.gradient += other.val * res.gradient
            other.gradient += self.val * res.gradient

        res.backward = _backward

        return res

    def __repr__(self) -> str:
        return f'val={self.val}, gradient={self.gradient}'

    def _gradientDemo(self, func):
        h = 0.0001
        return (func(self.val + h) - func(self.val)) / h

    def tanh(self):
        other = self.int_to_node(other)
        res = Node((math.exp(2*self.val) - 1) / (math.exp(2*self.val) + 1))

        def _backward():
            self.gradient += (1 - res.val**2) * res.val

        res.backward = _backward
        return res

    def relu(self):
        other = self.int_to_node(other)
        res = Node(max(0, self.val))

        def _backward():
            self.gradient += 1 if res.val > 0 else 0

        res.backward = _backward
        return res


a = Node(1)
b = Node(2)

print(a + 2)
