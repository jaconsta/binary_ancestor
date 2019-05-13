import unittest

from src.node import Node


class TestBinaryAncestor(unittest.TestCase):
    def test_can_find_ancestor(self):

        """
        (70, 84, 85)
        (70, 84, 78, 80)
        (70, 84, 78, 76)
        (70, 49, 54, 51)
        (70, 49, 37, 40)
        (70, 49, 37, 22)
        """

        tree = Node()
        # values = (84, 85, 78, 80, 76, 49, 54, 51, 37, 40, 22)
        values = [
            (70, 84, 85),
            (70, 84, 78, 80),
            (70, 84, 78, 76),
            (70, 49, 54, 51),
            (70, 49, 37, 40),
            (70, 49, 37, 22)
        ]
        [tree.insert(x) for y in values for x in y]

        self.assertEqual(tree.is_parent(40, 78), 70)
        self.assertEqual(tree.is_parent(51, 37), 49)
        self.assertEqual(tree.is_parent(76, 85), 84)

