"""
My solution. 44 ms
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        flag = False
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if mid - 1 >= 0 and nums[mid-1] < target and nums[mid] == target:
                start = mid
                flag = True
                break
            elif mid == 0 and nums[mid] == target:
                start = mid
                flag = True
                break

            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if mid + 1 < n and nums[mid + 1] > target and nums[mid] == target:
                end = mid
                break
            elif mid == n-1 and nums[mid] == target:
                end = mid
                break

            if target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        if not flag:
            return [-1, -1]
        return [start, end]


# nums = [5,7,7,8,8,10]
# target = 6
nums = [1]
target = 1
res = Solution().searchRange(nums, target)
print(res)