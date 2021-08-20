class Solution:
    
    def isValidCharacter(self, char):
        asciiChar = ord(char.lower())
        if asciiChar >= ord('a') and asciiChar <= ord('z'):
            return True
        if asciiChar >= ord('0') and asciiChar <= ord('9'):
            return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        
        
        while start <= end:
            
            while start < len(s) and not self.isValidCharacter(s[start]):
                start += 1
                
            while end > 0 and not self.isValidCharacter(s[end]):
                end -= 1
                           
            if start <= end:
                if s[start].lower() != s[end].lower():
                    return False
            else:
                return True
        
            start += 1
            end -= 1
        
        return True
            
            
        