"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""

from typing import *


class Solution:
    ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"]
    tens = [" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
    hands = ["", "", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        result = ""
        result += self.threeNumberToWords(num % 1000)
        num //= 1000
        if num % 1000:
            result = self.threeNumberToWords(num % 1000) + " Thousand" + result
        num //= 1000
        if num % 1000:
            result = self.threeNumberToWords(num % 1000) + " Million" + result
        num //= 1000
        if num % 1000:
            result = self.threeNumberToWords(num % 1000) + " Billion" + result
        return result[1:]

    def threeNumberToWords(self, num: int) -> str:
        result = ""
        if num >= 1000:
            result += self.ones[num // 1000] + " Thousand"
            num = num % 1000
        if num >= 100:
            result += self.ones[num // 100] + " Hundred"
            num = num % 100
        if num <= 9:
            return result + self.ones[num]
        elif num <= 19:
            return result + self.tens[num - 10]
        else:
            return result + self.hands[num // 10] + self.ones[num % 10]


A = Solution()
num = 1234567
A.numberToWords(num)
