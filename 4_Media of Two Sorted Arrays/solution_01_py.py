class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        imin = 0
        imax = len(nums1)
        m, n = len(nums1), len(nums2)
        half_len = int((m + n + 1) / 2)
        # 根据 nums1 进行切， nums2 要切的个数随之进行 half_len - i
        # i是 nums1 切割的位置
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < len(nums1) and nums2[j-1] > nums1[i]:
                # 说明此时nums1的切割位置i不合适，imin最起码要从i+1位置开始
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == len(nums1):
                    min_of_right = nums2[j]
                elif j == len(nums2):
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2


# nums1 = [1, 2]
# nums2 = [3, 4]

# nums1 = [6, 7, 8, 9, 10]
# nums2 = [1, 2, 3, 4, 5]

nums1 = [5, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 6]


aa = Solution().findMedianSortedArrays(nums1, nums2)
print(aa)