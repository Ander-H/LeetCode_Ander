class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            res_sum = target - numbers[i]
            res_nums = numbers[i+1:]
            pos = self.binary_search(res_nums, res_sum)
            if pos is not None:
                return i+1, pos+1+i+1

    def binary_search(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left <= right:
            pos = round((left + right) / 2)
            if numbers[pos] == target:
                return pos
            elif target < numbers[pos]:
                right = pos -1
            else:
                left = pos + 1
        return None
