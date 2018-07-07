class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_len = 1
                while current_num + 1 in nums:
                    current_num += 1
                    current_len += 1
                longest = max(longest, current_len)
        return longest