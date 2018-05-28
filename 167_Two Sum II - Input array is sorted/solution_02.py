# leetcode 中discuss的方法
# 使用dictionary，使用hashmap对于查找会更快


def twoSum(self, numbers, target):
    dic = {}
    for i in range(len(numbers)):
        if numbers[i] in dic:
            return [dic[numbers[i]] + 1, i + 1]
        else:
            dic[target - numbers[i]] = i


def twoSum(self, numbers, target):
    dic = {}
    for i in range(len(numbers)):
        if dic[target - numbers[i]] in dic:
            return dic[target - numbers[i]] + 1, i + 1
        else:
            dic[numbers[i]] = i