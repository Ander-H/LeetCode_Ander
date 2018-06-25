class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        while nums:
            i = nums.pop()
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        return a.pop()
