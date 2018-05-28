import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = str(math.sqrt(x))
        a = res.split('.')
        return int(a[0])