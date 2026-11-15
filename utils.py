import random

# Генерує список унікальних випадкових цілих чисел.
# Параметри:
# - min_count: мінімальна кількість елементів у списку
# - max_count: максимальна кількість елементів у списку
# - min_value: мінімальне значення елементів
# - max_value: максимальне значення елементів
# - unique_values: чи повинні значення бути унікальними (за замовчуванням True)
# Повертає список унікальних випадкових цілих чисел.
def generate_values(
    min_count=15,
    max_count=25,
    min_value=1,
    max_value=100,
    unique_values=True,
):
    count = random.randint(min_count, max_count)
    values = range(min_value, max_value + 1)

    if unique_values:
        return random.sample(values, count)

    return random.choices(values, k=count)


# Функція для виведення двійкового дерева у консоль.
# - root: корінь дерева
# Повертає рядок, що представляє дерево у вигляді текстової структури.
def format_tree(root):
    if root is None:
        return "(empty)"

    def build(node, prefix=""):
        result = ""

        children = []
        if node.left:
            children.append(("[L]", node.left))
        if node.right:
            children.append(("[R]", node.right))

        for index, (label, child) in enumerate(children):
            is_last = index == len(children) - 1
            connector = "+-- " if is_last else "|-- "

            value = child.key
            result += prefix + connector + label + " " + str(value) + "\n"

            extension = "    " if is_last else "|   "
            result += build(child, prefix + extension)

        return result

    return str(root.key) + "\n" + build(root).rstrip("\n")
