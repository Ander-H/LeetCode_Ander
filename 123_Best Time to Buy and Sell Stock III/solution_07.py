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
        dp = [0 for i in range(k + 1)]
        min_price = [prices[0] for i in range(k + 1)]
        min_price[0] = 0  # 此处记录min_price的list，第一个元素的值不影响结果

        for i in range(1, n):  # 相比于solution_05_06，减小了存储空间
            for j in range(1, k+1):
                min_price[j] = min(min_price[j], prices[i] - dp[j-1])
                dp[j] = max(dp[j], prices[i] - min_price[j])
        return dp[k]


prices = [3,3,5,0,0,3,1,4]
res = Solution().maxProfit(prices)
print(res)