"""
自己写的答案
使用深度优先搜索算法
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.dfs_node_sum(root, root.val, sum)

    def dfs_node_sum(self, node, node_sum, sum):
        if node.left is None and node.right is None:
            if node_sum == sum:
                return True
            else:
                return False
        if node.left is not None and node.right is None:
            return self.dfs_node_sum(node.left, node_sum + node.left.val, sum)
        elif node.left is None and node.right is not None:
            return self.dfs_node_sum(node.right, node_sum + node.right.val, sum)
        else:
            return self.dfs_node_sum(node.left, node_sum + node.left.val, sum) or \
                   self.dfs_node_sum(node.right, node_sum + node.right.val, sum)
