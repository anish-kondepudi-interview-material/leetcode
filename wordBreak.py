class Solution:
    
    def helper(self, s, wordSet, maxLen, memo):
        if len(s) == 0: return True
        if s in memo: return memo[s]
        for i in range(1,maxLen+1):
            if i > len(s): break
            word = s[:i]
            if word in wordSet:
                newWord = s[i:]
                memo[newWord] = self.helper(newWord,wordSet,maxLen, memo)
                if memo[newWord]:
                    return True
        return False
        
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        maxLen = 0
        for word in wordSet:
            maxLen = max(maxLen, len(word))
        return self.helper(s, wordSet, maxLen, memo)