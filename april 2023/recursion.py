def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)
