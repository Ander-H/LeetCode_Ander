class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right = len(nums) - 1
        left = 0
        pos = 0
        if len(nums) == 0:
            return 0

        while left <= right:
            pos = round((left + right) / 2)
            if nums[pos] == target:
                return pos
            elif target < nums[pos]:
                right = pos-1
            elif target > nums[pos]:
                left = pos + 1
        if nums[pos] > target:
            return pos
        else:
            return pos + 1
