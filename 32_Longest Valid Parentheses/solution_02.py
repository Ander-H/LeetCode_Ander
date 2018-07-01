"""
https://leetcode.com/problems/longest-valid-parentheses/solution/
动态规划方法
dp[i]:以第i个元素结尾的长度最长的substring
if s[i] == ')' and s[i-1] == '(':
    dp[i] = dp[i-2] + 2
if s[i] == '(':
    dp[i] = 0
if s[i] == ')' and s[i-1] == ')':
    if s[i - dp[i-1] - 1] == '(':
        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                dp[i] = 0
            elif i-1 >= 0 and s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            elif i-1 >= 0 and s[i] == ')' and s[i-1] == ')':
                if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
        return max(dp)
