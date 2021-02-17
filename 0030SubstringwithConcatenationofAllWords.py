"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        k = len(words[0])
        result = []
        for i in range(len(s) - k * len(words) + 1):
            now = words[::]
            if self.findeone(s[i:(k * len(words) + i)], now, k):
                result += [i]
        return result

    def findeone(self, s, words, k):
        """
        :param s:str
        :param words:List[str]
        :param k: int
        """
        if s == '':
            return True
        if s[0:k] in words:
            words.remove(s[0:k])
            return self.findeone(s[k:], words, k)
        else:
            return False
