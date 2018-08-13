"""
20180813
字节跳动的机试题
求取2维二值数组连通域的个数和面积
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        res = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    pixels = self.dfs(grid, i, j, 0)
                    count += 1
                    res.append([count, pixels])
        return res

    def dfs(self, grid, i, j, pixels):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return pixels
        grid[i][j] = '#'
        pixels += 1
        pixels = self.dfs(grid, i + 1, j, pixels)
        pixels = self.dfs(grid, i - 1, j, pixels)
        pixels = self.dfs(grid, i, j + 1, pixels)
        pixels = self.dfs(grid, i, j - 1, pixels)
        return pixels


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
