from utils import format_tree

# Реалізація AVL-дерева на основі конспекту.
class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.height = 1
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None

    def __str__(self):
        return format_tree(self)


def get_height(node: AVLNode | None) -> int:
    if not node:
        return 0
    return node.height


def get_balance(node: AVLNode | None) -> int:
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z: AVLNode) -> AVLNode:
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def right_rotate(y: AVLNode) -> AVLNode:
    x = y.left
    t3 = x.right

    x.right = y
    y.left = t3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


def insert(root: AVLNode | None, key: int) -> AVLNode:
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def create_avl_tree(values: list[int]) -> AVLNode | None:
    root = None
    for value in values:
        root = insert(root, value)
    return root
