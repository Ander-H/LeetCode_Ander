class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        child_index = 0
        cookie_index = 0
        while child_index < len(g) and cookie_index < len(s):
            if g[child_index] <= s[cookie_index]:
                child_index += 1
            cookie_index += 1
        return child_index