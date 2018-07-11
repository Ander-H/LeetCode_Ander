class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        flag = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                flag = 0
            dp[i][0] = flag
        flag = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                flag = 0
            dp[0][j] = flag
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] != 0:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i-1][j] != 0 and obstacleGrid[i][j-1] == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]
