"""
看题目的解答，应该不是说只能从中间把s1分开
"""


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) == 1 or len(s2) == 1:
            return s1 == s2

        m = len(s1)
        n = len(s2)
        half = int(m / 2)

        s1_1 = s1[0: half]
        s1_2 = s1[half:]
        s2_1 = s2[0:half]
        s2_2 = s2[half:]

        if not set(s1_1) == set(s2_1):
            s2_1 = s2[half:]
            s2_2 = s2[0: half]

        if not set(s1_1) == set(s2_1):
            return False
        else:
            judge_1 = self.isScramble(s1_1, s2_1)
            judge_2 = self.isScramble(s1_2, s2_2)
            return judge_1 and judge_2


s1 = 'cbbbc'
s2 = 'cbcbb'
res = Solution().isScramble(s1, s2)
print(res)