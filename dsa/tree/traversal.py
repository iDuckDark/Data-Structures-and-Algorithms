"""
traversal of binary tree
"""


def in_order(root):
    """
    in order traversal of binary tree. change location of visit to get
    other traversals
    """
    path = []
    if root:
        path = in_order(root.left)
        path.append(root.data)
        path.extend(in_order(root.right))
    return path
