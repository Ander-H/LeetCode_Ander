"""
top-down method
"""


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            tmp = [0 for i in range(len(triangle[i]))]
            for j in range(len(triangle[i])):
                if j == 0:
                    tmp[j] = triangle[i][j] + dp[j]
                elif j == len(triangle[i]) - 1:
                    tmp[j] = triangle[i][j] + dp[j-1]
                else:
                    tmp[j] = min(triangle[i][j] + dp[j-1], triangle[i][j] + dp[j])
            dp = tmp
        return min(dp)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = Solution().minimumTotal(triangle)
print(res)