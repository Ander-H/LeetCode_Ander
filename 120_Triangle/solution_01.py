"""
超时
"""


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0 for i in range(len(triangle))]
        for cols in range(len(triangle[-1])):
            dp[cols] = self.path(triangle, cols)
        return min(dp)

    def path(self, triangle, cols):
        total = 0
        if len(triangle) == 1:
            return triangle[0][0]
        else:
            # # 虽然时间都是超时，但是上面这段为什么不对呢？
            # # 好像就是不对的。在从底向上，在求取路径上所有数字之和最小的时候，不能只考虑选取上一层的紧邻最小值。
            # # 只考虑上面一层相邻两个数字的最小值，并不能该值所在的整个路径都是最小值
            # if cols == 0:
            #     total += self.path(triangle[0:-1], cols) + triangle[-1][cols]
            # elif cols == len(triangle[-1]) - 1:
            #     total += self.path(triangle[0:-1], cols-1) + triangle[-1][cols]
            # else:
            #     if triangle[-2][cols-1] < triangle[-2][cols]:
            #         total += self.path(triangle[0:-1], cols-1) + triangle[-1][cols]
            #     elif triangle[-2][cols-1] > triangle[-2][cols]:
            #         total += self.path(triangle[0:-1], cols) + triangle[-1][cols]
            #     else:
            #         total = min(total + self.path(triangle[0:-1], cols-1) + triangle[-1][cols],
            #                     total + self.path(triangle[0:-1], cols) + triangle[-1][cols])

            if cols == 0:
                total += self.path(triangle[0:-1], cols) + triangle[-1][cols]
            elif cols == len(triangle[-1]) - 1:
                total += self.path(triangle[0:-1], cols-1) + triangle[-1][cols]
            else:
                total = min(total + self.path(triangle[0:-1], cols-1) + triangle[-1][cols],
                            total + self.path(triangle[0:-1], cols) + triangle[-1][cols])
        return total


triangle = [[-3],[-9,7],[3,2,-4],[4,6,-1,9],[8,1,6,6,-4],[5,-5,5,7,-7,5],[-2,8,-5,1,0,-9,-9],[9,-5,0,-4,-5,-3,5,6],[-1,-1,-1,4,-2,-3,-4,-8,-7],[-2,3,-5,-6,-3,-6,5,4,-8,-9],[-8,-1,7,9,-2,-8,-1,3,-4,5,-5]]
res = Solution().minimumTotal(triangle)
print(res)