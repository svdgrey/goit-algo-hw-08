from bst import create_bst_tree
from avl import create_avl_tree
from utils import generate_values

# Знаходить мінімальне значення та кількість відвіданих вузлів у BST або AVL-дереві.
# Повертає (None, 0), якщо дерево порожнє.
def find_min(root) -> tuple[int | None, int]:
    if root is None:
        return None, 0

    current = root
    steps = 1

    while current.left is not None:
        current = current.left
        steps += 1

    return current.key, steps


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

    bst_min, bst_steps = find_min(bst_root)
    avl_min, avl_steps = find_min(avl_root)
    
    print(f"Найменше значення в BST дереві: {bst_min} (відвідано вузлів: {bst_steps})")
    print(f"Найменше значення в AVL дереві: {avl_min} (відвідано вузлів: {avl_steps})")


if __name__ == "__main__":
    main()

