class Solution:
    # Mihika's Bottom Up Dynamic Programming Solution
    def longestStrChain(self, words: List[str]) -> int:
        d = {}
        for word in words:
            d[word] = 1
        words = sorted(words, key=len)
        
        for word in words:
            for i in range(len(word)):
                prev = word[0:i] + word[i+1:len(word)]
                d[word] = max(d[word], d.get(prev, 0) + 1)
        return max(d.values())