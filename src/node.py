class Node:
    left = None
    right = None

    def __init__(self, data: int = None):
        self.data = data

    def insert(self, value: int):
        if self.data is None:
            self.data = value
            return

        if value == self.data:
            return
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value: int):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def is_parent(self, successor_a, successor_b):
        if successor_a <= self.data <= successor_b or successor_a >= self.data >= successor_b:
            return self.data
        elif successor_a < self.data:
            if self.left is None:
                return False
            else:
                return self.left.is_parent(successor_a, successor_b)
        else:
            if self.right is None:
                return False
            else:
                return self.right.is_parent(successor_a, successor_b)

    def clean(self):
        self.data = None
        self.right = None
        self.left = None
