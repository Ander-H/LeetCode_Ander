class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
                continue
            dp[i] = prices[i] - min_price
        return max(dp)


a = [7,1,5,3,6,4]
res = Solution().maxProfit(a)
print(res)