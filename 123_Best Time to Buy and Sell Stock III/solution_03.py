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
        if len(prices) == 0:
            return 0
        k = 2
        n = len(prices)
        dp = [[0 for i in range(n)] for j in range(k + 1)]
        for i in range(1, n):
            for j in range(1, k+1):
                min_price = prices[0]
                for m in range(1, i+1):
                    # 原网页中的这个界限 m 可以等于 i，应该不太对吧？在 m-1 以前完成j-1次交易，第m次是买入。
                    # 不过改进的方法，不用考虑这个界限问题
                    # 不过按照后面改进的方法，这个地方 i 应该可以等于 m
                    min_price = min(min_price, prices[m] - dp[j-1][m-1])
                dp[j][i] = max(dp[j][i-1], prices[i] - min_price)
        return dp[k][n-1]


prices = [3,3,5,0,0,3,1,4]
res = Solution().maxProfit(prices)
print(res)