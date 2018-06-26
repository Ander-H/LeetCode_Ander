"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36060/3-lines-in-Every-Language
BFS算法
"""


def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    depth = 0
    current_level = [root]

    while current_level:
        depth += 1
        next_level = []
        for node in current_level:
            left = node.left
            right = node.right
            if not left and not right:
                return depth
            if left:
                next_level.append(left)
            if right:
                next_level.append(right)
        current_level = next_level
    return depth