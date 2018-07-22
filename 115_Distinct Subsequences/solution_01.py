"""
借鉴97_Interleaving String 种的第一种迭代的方法，自己写的
逻辑之间要理清关系
"""


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        if s == t:
            return 1
        return self.num_Distinct(s, 0, t, 0)

    def num_Distinct(self, s, i, t, j):
        if i == len(s) and j < len(t):
            return 0

        if j == len(t):
            return 1

        count = 0
        for m in range(i, len(s)):
            if s[m] == t[j]:
                count += self.num_Distinct(s, m+1, t, j+1)
        return count


s = 'babgbag'
t = 'bag'
res = Solution().numDistinct(s, t)
print(res)