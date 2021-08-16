class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # In Built functions
        # return len(s.split()[-1])
        
        # No in-built functions
        lenWord = 0
        charIdx = len(s)-1
        
        while (s[charIdx] == " "): charIdx -= 1
        
        while (charIdx >= 0):
            if s[charIdx] == " ":
                return lenWord
            lenWord += 1
            charIdx -= 1

        return lenWord
    
        