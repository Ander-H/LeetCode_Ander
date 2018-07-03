class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        sum_all = reduce(lambda x, y: x + y, nums)
        sum_sigle = reduce(lambda x, y: x ^ y, nums)
        res = sum_sigle - (sum_all - sum_sigle) / 2
        return int(res)


nums = [2,2,3,2]
res = Solution().singleNumber(nums)
print(res)