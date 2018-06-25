# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.count(root)

    def count(self, node):
        layers_right = 0
        layers_left = 0
        if node.left is not None:
            layers_left = self.count(node.left) + 1
        if node.right is not None:
            layers_right = self.count(node.right) + 1
        if node.left is None and node.right is None:
            return 1
        return max(layers_left, layers_right)

