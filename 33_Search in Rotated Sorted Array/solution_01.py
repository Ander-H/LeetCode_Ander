"""
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms

It is difficult to judge and discuss every situation and edge cases.
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2  # 这个样子去中间值，一定会更靠近low，例如（1+2）//2 = 1

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


# nums = [4,5,6,7,0,1,2]
nums = [1, 3]
target = 3
res = Solution().search(nums, target)
print(res)
