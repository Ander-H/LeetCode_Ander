"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution

dp[k][i] = max(dp[k][i-1], price[i] - (price[j] - dp[k-1][j-1]))
or
dp[k][i] = max(dp[k][i-1], price[i] - price[j] + dp[k-1][j-1] )   (j=0...i-1)
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2
        n = len(prices)
        dp = [[0] * n] * k

        for i in range(n):
            min_price = prices[0]
            for j in range(k):
                min_price = min(min_price, prices[i] - dp[j-1][i])
                dp[k][i] = max(dp[k][i-1], prices[i] - min_price)
        return dp[k][n-1]
