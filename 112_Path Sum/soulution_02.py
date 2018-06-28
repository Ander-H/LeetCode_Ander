"""
自己写的答案
使用广度优先搜索算法
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
        current_level = []
        sum_dict = {}
        current_level.append(root)
        sum_dict[root] = root.val

        while current_level:
            tmp_dict = {}
            next_level = []
            for node in current_level:
                if node.left is None and node.right is None:
                    if sum_dict[node] == sum:
                        return True
                if node.left is not None:
                    cur_sum = sum_dict[node] + node.left.val
                    next_level.append(node.left)
                    tmp_dict[node.left] = cur_sum
                if node.right is not None:
                    cur_sum = sum_dict[node] + node.right.val
                    next_level.append(node.right)
                    tmp_dict[node.right] = cur_sum
            current_level = next_level
            sum_dict = tmp_dict
        return False
