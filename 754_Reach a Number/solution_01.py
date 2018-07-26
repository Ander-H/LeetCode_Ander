"""
这个思路是不对的
"""


class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = abs(target)
        pos = 0
        step = 0
        while pos <= target:
            step += 1
            pos += step
            if pos == target:
                return step
        if target - (pos - step) <= (pos - target):
            step = step - 1 + (target - (pos - step)) * 2
        else:
            step = step + (pos - target) * 2
        return step