"""
自己写的答案，不对!!!
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left_parenthesis_counter = 0
        right_parenthesis_counter = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_parenthesis_counter += 1
            else:
                right_parenthesis_counter += 1

            if left_parenthesis_counter == 0 and right_parenthesis_counter == 1:
                left_parenthesis_counter = 0
                right_parenthesis_counter = 0
            elif right_parenthesis_counter > left_parenthesis_counter:
                max_length = max(max_length, left_parenthesis_counter * 2)
            elif i == len(s) - 1:
                max_length = max(max_length, right_parenthesis_counter * 2)
        return max_length

