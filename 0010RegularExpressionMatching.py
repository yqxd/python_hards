"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false


Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
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
        d = [[False for i in range(m + 1)] for j in range(n + 1)]
        w = 2
        while True:
            if w <= m and p[w - 1] == '*':
                d[0][w] = True
                w = w + 2
            else:
                break
        d[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    if p[j - 2] == '.':
                        w = False
                        for k in range(i, -1, -1):
                            if d[k][j - 2]:
                                w = True
                                break
                        d[i][j] = w
                    else:
                        w = False
                        if d[i][j - 2]:
                            w = True
                        else:
                            for k in range(i, 0, -1):
                                if s[k - 1] == p[j - 2]:
                                    if d[k - 1][j - 2]:
                                        w = True
                                        break
                                else:
                                    break
                        d[i][j] = w
                elif p[j - 1] == '.':
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = d[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return d[n][m]
