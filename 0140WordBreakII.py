class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # if len(s) == 0:
        #     return [""]
        # result = []
        # for word in wordDict:
        #     if s[0:len(word)] == word:
        #         if len(s) == len(word):
        #             result += [word]
        #         else:
        #             for subresult in self.wordBreak(s[len(word)::], wordDict):
        #                 result += [word + " " + subresult]
        # return result
        all_chars_in_s = list(set(s))
        all_chars_in_Dict = set("".join(wordDict))
        for c in all_chars_in_s:
            if c not in all_chars_in_Dict:
                return []

        if (len(s) == 0):
            return []
        else:
            res = []
            for i in range(1, len(s) + 1):
                if s[0: i] in wordDict:
                    def addS(oldS):
                        print(s[0: i])
                        return s[0: i] + " " + oldS

                    temp_res = self.wordBreak(s[i:], wordDict)
                    if (len(s[i:]) == 0):
                        temp_res = [s[0: i]]
                    else:
                        temp_res = map(addS, temp_res)
                    res += temp_res
            return res


A = Solution()

s = "aaaaaaaaaaaaaa"
words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(A.wordBreak(s, words))

s = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
