class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = set()
        self.gradient = float('inf')

    def __add__(self, other):
        res = self.val + other.val
        backward = 2

        self.children.add(other)
        return res

    def __mul__(self, other):
        res = self.val * other.val
        self.children.add(other)
        return res

    def __pow__(self, other):
        res = self.val ** other.val
        self.children.add(other)
        return res

    def __repr__(self) -> str:
        return f'val={self.val}'

    def gradient(self, func):
        h = 0.0001
        return (func(self.val + h) - func(self.val)) / h

    def relu(self):
        return max(0, self.val)
