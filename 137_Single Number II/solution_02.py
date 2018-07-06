"""

"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in nums:
            a = a ^ i & ~b
            b = b ^ i & ~a
        return a


nums = [2,2,3,2]
res = Solution().singleNumber(nums)
print(res)