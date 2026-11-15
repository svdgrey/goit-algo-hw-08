from utils import format_tree

# Базова реалізація двійкового дерева пошуку з конспекту.
class Node:
    def __init__(self, key: int):
        self.left: Node | None = None
        self.right: Node | None = None
        self.key = key

    def __str__(self):
        return format_tree(self)


def insert(root: Node | None, key: int) -> Node:
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def create_bst_tree(values: list[int]) -> Node | None:
    root = None
    for value in values:
        root = insert(root, value)
    return root
