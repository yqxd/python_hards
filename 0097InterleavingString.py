"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        d = {}
        d[(0, 0)] = True
        d[(0, 0)] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                d[i, 0] = True
            else:
                for j in range(i, len(s1) + 1):
                    d[j, 0] = False
                break
        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1]:
                d[0, j] = True
            else:
                for i in range(j, len(s2) + 1):
                    d[0, i] = False
                break
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                d[i, j] = (d[i - 1, j] and s1[i - 1] == s3[i + j - 1]) or (d[i, j - 1] and s2[j - 1] == s3[i + j - 1])
        return d[len(s1), len(s2)]
