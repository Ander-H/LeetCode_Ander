"""
根据一元二次方程的求解公式直接求解
"""


class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        import math
        target = abs(target)
        n = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)
        sum = n * (n + 1) / 2
        res = sum - target
        if sum == target:
            return n
        else:
            return n if res % 2 == 0 else n + 1 + n % 2
