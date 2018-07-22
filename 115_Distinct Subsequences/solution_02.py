"""

"""


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) == 0 or len(s) == 0:
            return 0
        dp = [[0 for j in range(len(s))] for i in range(len(t))]
        for i in range(len(t)):
            for j in range(i, len(s)):
                if i == 0 and t[i] == s[j]:
                    dp[i][j] = dp[i][j-1] + 1
                elif s[j] == t[i]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(t)-1][len(s)-1]


s = 'babgbag'
t = 'bag'
res = Solution().numDistinct(s, t)
print(res)