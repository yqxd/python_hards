"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.



Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true


Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


# class Solution(object):
#     num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     d = {
#         ('n', '.'): ['n', 'o'], ('n', 'e'): ['n'],
#         ('n', '+'): ['n'], ('.', 'n'): ['+', 'o'],
#         ('e', 'n'): ['+', 'o'], ('+', 'n'): ['+', 'e', '.', 'o'],
#         ('+', '.'): ['n']
#     }
#
#     def isNumber(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if s == '':
#             return True
#         else:
#             p = 0
#             s = s.replace("-", "+")
#             before, p = self.getNum(s, p)
#             if before == 'n':
#                 inc = ['+', 'e', '.', 'o']
#             elif before == ".":
#                 inc = ['n']
#             elif before == "+":
#                 inc = ['n']
#             else:
#                 return False
#             while p < len(s):
#                 after, p = self.getNum(s, p)
#                 if after not in inc:
#                     return False
#                 else:
#                     inc = self.d[(before, after)]
#                     before = after
#             if 'o' in inc:
#                 return True
#             else:
#                 return False
#
#     def getNum(self, s, p):
#         if s[p] not in self.num:
#             return s[p], p + 1
#         while p < len(s) and s[p] in self.num:
#             p += 1
#         return 'n', p
#
# A = Solution()
# print(A.isNumber("."))


class Solution(object):
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace("-", "+")
        s = s.replace("E", "e")
        s = s.replace("n", "m")
        l = self.getNum(s, 0)
        if l in [
            "",
            "n",
            ".n", "+n", "n.",
            "n.n", "nen", "+.n", "+n.",
            "+n.n", "+nen", ".nen", "n.en", "ne+n",
            "n.nen", "+.nen", ".ne+n", "+n.en", "n.e+n", "+ne+n",
            "+n.nen", "n.ne+n", "+.ne+n",
            "+n.ne+n"
        ]:
            return True
        else:
            return False

    def getNum(self, s, p):
        if p >= len(s):
            return ""
        elif s[p] not in self.num:
            return s[p] + self.getNum(s, p+1)
        while p < len(s) and s[p] in self.num:
            p += 1
        return 'n' + self.getNum(s, p)

A = Solution()
print(A.isNumber("1.431352e7"))