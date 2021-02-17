"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        valid = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack += [i]
            else:
                if stack != []:
                    stack.pop(-1)
                    if stack == []:
                        if maxlen < i - valid + 1:
                            maxlen = i - valid + 1
                    else:
                        now = stack[-1] + 1
                        if maxlen < i - now + 1:
                            maxlen = i - now + 1
                else:
                    valid = i + 1
                    stack = []
        return maxlen

