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
        imin, imax = 0, len(nums1)-1

        while True:
            i = int((imin + imax) / 2)
            j = half_len - i - 2
            if nums1[i] > nums2[j + 1] and i != m:
                imax = i
            elif nums1[i+1]  < nums2[j] and i != m:
                imax = i + 1
            else:
                if (m+n)%2 != 0:
                    return max(nums1[i], nums2[j])
                else:




nums1 = [1, 2]
nums2 = [3, 4]
aa = Solution().findMedianSortedArrays(nums1, nums2)
print(aa)