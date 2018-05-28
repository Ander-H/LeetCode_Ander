class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            pos = int((left + right) / 2)
            if nums[pos] == target:
                return pos
            elif target > nums[pos]:
                left = pos + 1
            else:
                right = pos - 1
        return left


a = [1,3,5,6]
pos = Solution().searchInsert(a, 7)
print(pos)