# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            res = []
            res = self.get_node_val(root, 0, res)
            res.reverse()
        return res

    def get_node_val(self, node, layer, res):
        if node != None:
            if len(res) < layer + 1:
                res.append([])
            self.get_node_val(node.left, layer+1, res)
            self.get_node_val(node.right, layer+1, res)
            res[layer].append(node.val)
            return res

