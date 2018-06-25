"""
https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better
second solution
the time complexity is O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs_depth(root) != -1

    def dfs_depth(self, root):
        if root is None:
            return 0

        left_height = self.dfs_depth(root.left)
        if left_height == -1:
            return -1
        right_height = self.dfs_depth(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
