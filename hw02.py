from bst import create_bst_tree
from avl import create_avl_tree
from utils import generate_values


# Обчислює суму всіх значень у BST або AVL-дереві.
def tree_sum(root) -> int:
    if root is None:
        return 0

    return root.key + tree_sum(root.left) + tree_sum(root.right)

def main():

    values = generate_values(min_count=15, max_count=25, min_value=1, max_value=99)
    bst_root = create_bst_tree(values)
    avl_root = create_avl_tree(values)

    print(f"Значення: {values}")
    print()

    print("BST Дерево:")
    print(bst_root)
    print()

    print("AVL Дерево:")
    print(avl_root)
    print()

    print(f"Сума всіх значень в BST дереві: {tree_sum(bst_root)}")
    print(f"Сума всіх значень в AVL дереві: {tree_sum(avl_root)}")

if __name__ == "__main__":
    main()
    