class Node:
    def __init__(self, x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None


def CountLeaves(root):
    if root is None:
        return 0
    if root.Lchild is None and root.Rchild is None:
        return 1
    return CountLeaves(root.Lchild) + CountLeaves(root.Rchild)


def Count1Deg(root):
    if root is None:
        return 0
    c = 0
    if (root.Lchild is None) != (root.Rchild is None):
        c = 1
    return c + Count1Deg(root.Lchild) + Count1Deg(root.Rchild)


def Count2Deg(root):
    if root is None:
        return 0
    c = 0
    if root.Lchild is not None and root.Rchild is not None:
        c = 1
    return c + Count2Deg(root.Lchild) + Count2Deg(root.Rchild)


def SumTree(root):
    if root is None:
        return 0
    return root.Data + SumTree(root.Lchild) + SumTree(root.Rchild)


def CountNodes(root):
    if root is None:
        return 0
    return 1 + CountNodes(root.Lchild) + CountNodes(root.Rchild)


def PreOrder(root):
    if root is None:
        return
    print(root.Data)
    PreOrder(root.Lchild)
    PreOrder(root.Rchild)


def Search(root, target):
    if root is None:
        return False
    if root.Data == target:
        return True
    return Search(root.Lchild, target) or Search(root.Rchild, target)


def MaxTree(root):
    if root is None:
        return float("-inf")
    return max(root.Data, MaxTree(root.Lchild), MaxTree(root.Rchild))