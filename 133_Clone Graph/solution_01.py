"""
https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        from collections import deque
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
    