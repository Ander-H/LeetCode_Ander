"""
https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution
动态规划不一定要直接对全体、每个维度一起做，
也可以只对其中一个维度做，然后另一个维度使用其他的方法
"""


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0 for j in range(n)]
        right = [n for j in range(n)]
        height = [0 for j in range(n)]

        max_area = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    cur_left = j + 1
                    left[j] = 0

            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    cur_right = j
                    right[j] = n

            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
        return max_area


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
res = Solution().maximalRectangle(matrix)
print(res)