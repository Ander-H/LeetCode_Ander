"""

"""


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
                    f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False


# s1 = 'cbbbc'
# s2 = 'cbcbb'

s1 = 'baa'
s2 = 'aba'

res = Solution().isScramble(s1, s2)
print(res)