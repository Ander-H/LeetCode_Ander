class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '#'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
"""
11000
11000
00100
00011
"""
# grid = input().split('\n')

import sys
grid = list(map(lambda x: [char for char in x.strip()], sys.stdin.readlines()))
res = Solution().numIslands(grid)
print(res)
