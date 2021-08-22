class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Handle Edge Case
        if len(s) <= 1:
            return len(s)
        
        maxLen = 0
        
        seen = set()
        ptr1 = 0
        ptr2 = 0
        
        
        while True:
            
            # Increment ptr2 until [ptr1,ptr2) is not longer a substring
            while ptr2 < len(s) and s[ptr2] not in seen:
                seen.add(s[ptr2])
                ptr2 += 1

            # Update max substring length
            maxLen = max(maxLen,len(seen))
            
            # If end of string reached, return
            if ptr2 == len(s):
                return maxLen
            
            # Increment ptr1 until [ptr1,ptr2) is again a substring
            while s[ptr1] != s[ptr2]:
                seen.remove(s[ptr1])
                ptr1 += 1
            ptr1 += 1
            seen.remove(s[ptr2])
            
            
        
        
        