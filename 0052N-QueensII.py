"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self.findone([], n, n)
        return len(result)

    def findone(self, lists, k, n):
        if k == 0:
            return [lists]
        else:
            result = []
            for i in range(n):
                if self.check(lists, i):
                    result += self.findone(lists + [i], k - 1, n)
            return result

    def check(self, lists, i):
        if i in lists:
            return False
        for j in range(len(lists)):
            if abs(len(lists) - j) == abs(i - lists[j]):
                return False
        return True
