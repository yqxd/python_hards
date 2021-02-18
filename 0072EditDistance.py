"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        m = len(word1)
        n = len(word2)
        for i in range(m + 1):
            d[i, 0] = i
        for j in range(n + 1):
            d[0, j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                minnum = d[i - 1, j - 1] + 1
                if word1[i - 1] == word2[j - 1]:
                    minnum -= 1
                minnum = min(minnum, d[i - 1, j] + 1, d[i, j - 1] + 1)
                d[i, j] = minnum
        return d[m, n]