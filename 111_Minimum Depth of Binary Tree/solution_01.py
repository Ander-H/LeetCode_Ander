"""
自己写的答案
应该属于dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dfs_depth(root)

    def dfs_depth(self, node):
        if node.left is None and node.right is None:
            return 1
        elif node.left is not None and node.right is None:
            left_mini_height = self.dfs_depth(node.left) + 1
            return left_mini_height
        elif node.left is None and node.right is not None:
            right_mini_height = self.dfs_depth(node.right) + 1
            return right_mini_height
        else:
            left_mini_height = self.dfs_depth(node.left) + 1
            right_mini_height = self.dfs_depth(node.right) + 1
            return min(left_mini_height, right_mini_height)
