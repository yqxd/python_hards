"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        d = [0, 0]
        for index1 in range(2, len(s) + 1):
            if self.isP(s[:index1]):
                MP = 0
            else:
                MP = index1 - 1
                for index2 in range(1, index1):
                    if self.isP(s[index2:index1]):
                        MP = min(MP, 1 + d[index2])
            d.append(MP)
        return d[-1]

    def isP(self, s):
        return s[::-1] == s


A = Solution()
print(A.minCut("aab"))
