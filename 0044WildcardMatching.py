"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false


Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        d = [[-1 for j in range(m + 1)] for i in range(n + 1)]
        d[0][0] = True
        for i in range(1, n + 1):
            d[i][0] = False
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                d[0][i] = True
            else:
                for k in range(i, m + 1):
                    d[0][k] = False
                break
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '?':
                    d[i][j] = d[i - 1][j - 1]
                elif p[j - 1] == '*':
                    d[i][j] = d[i - 1][j - 1] or d[i][j - 1] or d[i - 1][j]
                elif p[j - 1] == s[i - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = False
        return d[n][m]
