class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for i in range(round(len(str(x)) / 2)):
            if str(x)[i] != str(x)[-i-1]:
                return False
        return True

a = Solution()
print(a.isPalindrome(1000021))
print('###')