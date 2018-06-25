"""
https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better
first solution
the time complexity is O(n^2)
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
        if root is None:
            return True
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)

        return abs(left_height - right_height) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
