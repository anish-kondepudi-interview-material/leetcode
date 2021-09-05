class Solution:
    # O(S) where S in length of String, s
    def exists(self, s, word):
        i = 0
        for c in s:
            if word[i] == c:
                i += 1
            if i == len(word): return True
        return False
    
    # (N*S) where N is length of array, dictionary
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longestWord = ""
        for word in dictionary:
            if self.exists(s,word):
                if len(word) > len(longestWord):
                    longestWord = word
                elif len(word) == len(longestWord) and word < longestWord:
                    longestWord = word
        return longestWord
                    
        