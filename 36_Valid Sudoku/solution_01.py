"""
https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        import collections
        return 1 == max(
            list(collections.Counter(
                x
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'
                for x in [(c, i), (j, c), (i // 3, j // 3, c)]
            ).values()) + [1])


board = [
  ["9","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
res = Solution().isValidSudoku(board)
print(res)