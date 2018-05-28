# LeetCode中discuss的方法
# For more info about this method plz read: Square Roots via Newton’s Method
# 牛顿迭代法求解平方根


def getRoot(a, n=2):
    if a * n == 0:
        return 0
    x0, x1 = a, 0
    while x0 > a / (x0 ** (n - 1)):  # prevent overflow
        x1 = x0 - (x0 ** n - a) / (n * x0 ** (n - 1))
        if x0 == x1:
            break
        x0 = x1
    return x0
