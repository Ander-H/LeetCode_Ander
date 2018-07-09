class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pointer_s, pointer_p, match, starIdx = 0, 0, 0, -1
        while pointer_s < len(s):
            if pointer_p < len(p) and (p[pointer_p] == s[pointer_s] or p[pointer_p] == '?'):
                pointer_s += 1
                pointer_p += 1
            elif pointer_p < len(p) and p[pointer_p] == '*':
                starIdx = pointer_p
                match = pointer_s
                pointer_p += 1
            elif starIdx != -1:
                pointer_p = starIdx + 1
                match += 1
                pointer_s = match
            else:
                return False
        while pointer_p < len(p) and p[pointer_p] == '*':
            pointer_p += 1
        return pointer_p == len(p)


s = 'adceb'
p = '*a*b'
res = Solution().isMatch(s, p)
print(res)

