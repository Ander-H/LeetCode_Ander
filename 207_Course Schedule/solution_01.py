class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        # construct graph
        graph = {i: set() for i in range(numCourses)}
        in_degrees = {i: 0 for i in range(numCourses)}

        for edge in prerequisites:
            graph[edge[0]].add(edge[1])
            in_degrees[edge[1]] += 1

        # init var
        q = deque()
        visited = set()

        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(index)

        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.add(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)
        return len(visited) == numCourses

