"""
自己写的答案
错误的
考虑使用广度优先搜索算法，里面有错误
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
                    if cur_sum <= sum:  # 这个地方是不对的，可能在这一层大于sum，但是下一层是负数的话，可能就又小于等于sum了
                        next_level.append(node.left)
                        tmp_dict[node.left] = cur_sum
                if node.right is not None:
                    cur_sum = sum_dict[node] + node.right.val
                    if cur_sum <= sum:
                        next_level.append(node.right)
                        tmp_dict[node.right] = cur_sum
            current_level = next_level
            sum_dict = tmp_dict
        return False
