class Node:
    def __init__(self, val) -> None:
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __mul__(self, other):
        return self.val * other.val

    def gradient(self, func):
        h = 0.0001
        return (func(self.val + h) - func(self.val)) / h

    def __repr__(self) -> str:
        return 'hello'