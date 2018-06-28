"""
20180628_复习
还是很难，边界条件分不清楚
此处写的还不是最完善的答案，查看solution_01_py.py
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2, m, n = nums2, nums1, n, m
        half_len = int((m+n+1)/2)
        imin, imax = 0, len(nums1)

        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = min(nums1[0], nums2[j-1])
                elif j == 0:
                    max_of_left = min(nums1[i-1], nums2[j])
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = max(nums1[i-1], nums2[j])
                elif j == n:
                    min_of_right = max(nums1[i], nums2[j-1])
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2


# nums1 = [1, 2]
# nums2 = [3, 4]

nums1 = [5, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 6]

aa = Solution().findMedianSortedArrays(nums1, nums2)
print(aa)