"""
Solution
Brute Force
"""


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.is_Interleave(s1, 0, s2, 0, '', s3)

    def is_Interleave(self, s1, i, s2, j, res, s3):
        if i == len(s1) and j == len(s2) and res == s3:
            return True
        ans = False
        if i < len(s1):
            ans = ans or self.is_Interleave(s1, i+1, s2, j, res + s1[i], s3)
        if j < len(s2):
            ans = ans or self.is_Interleave(s1, i, s2, j+1, res+s2[j], s3)
        return ans
