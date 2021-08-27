class Solution:
    
    def expand(self, left, right, s):
        size = -1 if left==right else 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            size += 2
            left -= 1
            right += 1
        return size
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxSize = 0
        start = -1
        end = -1
        
        for i in range(len(s)-1):
            
            tempMax = self.expand(i,i,s)
            if tempMax > maxSize:
                maxSize = tempMax
                start = i-tempMax//2
                end = i+tempMax//2
            
            tempMax = self.expand(i,i+1,s)
            if tempMax > maxSize:
                maxSize = tempMax
                start = i - (tempMax//2 - 1)
                end = i+1 + (tempMax//2 - 1)
                
        return s[start:end+1]