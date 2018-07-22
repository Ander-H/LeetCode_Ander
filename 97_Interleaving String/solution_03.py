"""

"""


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] and s3[j-1] == s2[j-1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] and s3[i-1] == s1[i-1]
                else:
                    dp[i][j] = dp[i-1][j] and s3[i+j-1] == s1[i-1] or (dp[i][j-1] and s3[i+j-1] == s2[j-1])
        return dp[len(s1)][len(s2)]


s1 = 'db'
s2 = 'b'
s3 = 'cbb'
res = Solution().isInterleave(s1, s2, s3)
print(res)