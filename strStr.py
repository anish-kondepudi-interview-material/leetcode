class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == None or haystack == None: return -1
        
        if needle == haystack: return 0
        if len(needle) > len(haystack): return -1
    
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        
        for i in range(lenHaystack-lenNeedle+1):
            if haystack[i:i+lenNeedle] == needle:
                return i
        
        return -1
            
        