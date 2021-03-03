class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
        for word in wordDict:
            if s[0:len(word)] == word:
                for subresult in self.wordBreak(s[len(word)::], wordDict):
                    result += [word + " " + subresult]
        return result


A = Solution()
print(A.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
