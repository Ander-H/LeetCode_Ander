"""
这个思路是错误的，并是倒序比较存在不存在，就可判断 Interleaving String 的
比如：
s1: a
s2: aba
s3: aaba

"""


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        while len(s3) >= 1:
            if len(s1) == 0:
                return s3 == s2
            elif len(s2) == 0:
                return s3 == s1
            else:
                if s1[-1] == s3[-1]:
                    s1 = s1[0:-1]
                    s3 = s3[0:-1]
                elif s2[-1] == s3[-1]:
                    s2 = s2[0:-1]
                    s3 = s3[0:-1]
                else:
                    return False
        return True