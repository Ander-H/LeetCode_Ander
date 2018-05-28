# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None and root.right is not None:
            return False
        elif root.left is not None and root.right is None:
            return False
        else:
            return self.symmetric(root.left, root.right)

    def symmetric(self, p, q):
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        else:
            if p.val == q.val:
                return True and self.symmetric(p.left, q.right) and self.symmetric(p.right, q.left)
            else:
                return False

