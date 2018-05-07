# 错误解法，没有考虑二叉树的性质

import math


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if len(t) == 0:
            return None
        t = list(map(str, t))
        num_root_layer = math.floor(math.log(len(t), 2))
        self.num_root_node = int(math.pow(2, num_root_layer) - 1)
        self.last_layer_node = int(math.pow(2, num_root_layer -1))
        t = t + ['None'] * int((math.pow(2, num_root_layer + 1) - 1 -len(t)))
        a = self.tree(t, 1)
        while a.find('None') != -1:
            index = a.find('None')
            if a[index-2].isdigit():
                a = a[:index] + a[index+4:]
            else:
                a = a[:index-1] + a[index+5:]
        while a[-3:-1] == '()':
            a = a[:-3] + a[-1]
        return a

    def tree(self, t, index):
        return self.tree_iter(t, index)

    def tree_iter(self, t, index):
        if (self.num_root_node - self.last_layer_node + 1) <= index <= self.num_root_node:
            return t[index-1]+'(' + t[2*index-1] + ')' + '(' + t[2*index] + ')'
        return t[index-1] + '(' + self.tree_iter(t, index * 2) + ')' + \
               '(' + self.tree_iter(t, index * 2 + 1) + ')'


t = [1,2,3,4]
result = Solution().tree2str(t)