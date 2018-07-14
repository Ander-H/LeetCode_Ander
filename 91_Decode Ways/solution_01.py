class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] == '0':
                return 0
            elif s[i] == '0' and int(s[i-1]+s[i]) > 26:
                return 0
            elif s[i] == '0':
                dp[i+1] = dp[i-1]
            elif s[i-1] == '0':
                dp[i+1] = dp[i]
            elif int(s[i-1]+s[i]) > 26:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[len(s)]
