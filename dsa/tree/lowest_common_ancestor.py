"""find lowest common ancestor of two nodes in a tree"""
from collections import namedtuple

TreeNode = namedtuple("TreeNode", "data left right")


def lowest_common_ancestor(root, i, j):
    """
    We traverse to the bottom, and once we reach a node which matches one
    of the two nodes, we pass it up to its parent. The parent would then test
    its left and right subtree if each contain one of the two nodes. If yes,
    then the parent must be the LCA and we pass its parent up to the root. If
    not, we pass the lower node which contains either one of the two nodes
    (if the left or right subtree contains either p or q), or NULL (if both
    the left and right subtree does not contain either p or q) up.

    Time: O(n)
    """
    if root is None:
        return None

    if root.data in (i.data, j.data):
        return root

    left = lowest_common_ancestor(root.left, i, j)
    right = lowest_common_ancestor(root.right, i, j)

    if left and right:
        return root

    return left if left else right


def test():
    """run test cases"""
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None)),
        TreeNode(7, TreeNode(6, None, None), TreeNode(8, None, None)),
    )

    lca = lowest_common_ancestor(root, root.left.left, root.right.left)
    print(lca.data)


if __name__ == "__main__":
    test()
