# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        res = self.genTree(1, n)
        return res

    def genTree(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res

        if start == end:
            res.append(TreeNode(end))
            return res

        for i in range(start, end+1):
            left = self.genTree(start, i-1)
            right = self.genTree(i+1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    res.append(root)
        return res


n = 10
res = Solution().generateTrees(3)