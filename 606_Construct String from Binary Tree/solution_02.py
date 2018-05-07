# leetcode solution中的解法
# 首先需要知道树的数据结构，采用递归的方法，注意一些边界条件的判断

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        elif t.left is None and t.right is None:
            return str(t.val)
        elif t.right is None:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        else:
            return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'

