

class Solution:

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [x for x in range(-1, n)]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i + r1 < n and i - r1 >= 0 and s[i-r1] == s[i+r1]:  # odd palindrome
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1] + 1)
                r1 += 1
            while i + r2 + 1 < n and i - r2 >= 0 and s[i-r2] == s[i+r2+1]:  # even palindrome
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2] + 1)
                r2 += 1
        return cut[-1]


s = 'efe'
res = Solution().minCut(s)
print(res)
