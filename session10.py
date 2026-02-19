class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def count_degree_one(node):
    if node is None:
        return 0
    count = 0
    if (node.left is None) != (node.right is None):
        count = 1
    return count + count_degree_one(node.left) + count_degree_one(node.right)


def count_degree_two(node):
    if node is None:
        return 0
    count = 0
    if node.left is not None and node.right is not None:
        count = 1
    return count + count_degree_two(node.left) + count_degree_two(node.right)


def sum_tree(node):
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def search_tree(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    return search_tree(node.left, target) or search_tree(node.right, target)


def max_tree(node):
    if node is None:
        return float("-inf")
    return max(node.data, max_tree(node.left), max_tree(node.right))