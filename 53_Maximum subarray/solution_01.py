# 1. 动态规划的关键点在于，不是 0-i 之间和最大的连续子序列，而是以 i 为结尾的和最大的连续子序列
# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, length):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_sum = max(max_sum, dp[i])
        return max_sum
