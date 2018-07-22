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
        dp = [[0 for j in range(len(s))] for i in range(2)]
        for i in range(len(t)):
            for j in range(i, len(s)):
                if i == 0 and t[i] == s[j]:
                    dp[1][j] = dp[1][j-1] + 1
                elif s[j] == t[i]:
                    dp[1][j] = dp[0][j-1] + dp[1][j-1]
                else:
                    dp[1][j] = dp[1][j-1]
            dp[0] = dp[1]
            dp[1] = [0 for _ in range(len(s))]
        return dp[0][len(s)-1]


s = 'babgbag'
t = 'bag'
res = Solution().numDistinct(s, t)
print(res)