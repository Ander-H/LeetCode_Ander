"""
bottom-up method
https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle
"""


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = Solution().minimumTotal(triangle)
print(res)