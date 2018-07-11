class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = 0
        for i in range(m):
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1
        for j in range(1, n):
            for i in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[n-1][m-1]


m = 3
n = 2
res = Solution().uniquePaths(m, n)
print(res)
