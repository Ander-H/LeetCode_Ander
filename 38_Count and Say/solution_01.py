"""
https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import re
        s = '1'
        for _ in range(n-1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s


n = 2
res = Solution().countAndSay(n)
print(n)
