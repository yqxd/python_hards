"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"


Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == '' or t == '':
            return ''
        d = {}
        o = {}
        for i in t:
            if i not in d:
                d[i] = 0
                o[i] = 1
            else:
                o[i] += 1
        nownum = 0
        m = len(t)
        left = 0
        right = 0
        minnum = float('Inf')
        minstr = ""
        while True:
            if right == len(s) + 1:
                return minstr
            elif nownum == m:
                if minnum > right - left:
                    minnum = right - left
                    minstr = s[left:right]
                if s[left] in d:
                    d[s[left]] -= 1
                    if d[s[left]] < o[s[left]]:
                        nownum -= 1
                left += 1
            else:
                right += 1
                if right == len(s) + 1:
                    return minstr
                if s[right - 1] in d:
                    d[s[right - 1]] += 1
                    if d[s[right - 1]] <= o[s[right - 1]]:
                        nownum += 1
