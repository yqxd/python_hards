class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        result = []
        for word in wordDict:
            if s[0:len(word)] == word:
                if len(s) == len(word):
                    result += [word]
                else:
                    for subresult in self.wordBreak(s[len(word)::], wordDict):
                        result += [word + " " + subresult]
        return result


A = Solution()
print(A.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
