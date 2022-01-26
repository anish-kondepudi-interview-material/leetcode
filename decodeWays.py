class Solution:
    
    def helper(self, i, s, memo):
        # Base Cases
        if i < len(s) and s[i] == '0': 
            return 0
        if i in memo: 
            return memo[i]
        
        # Recurse
        numDecodings = self.helper(i+1,s,memo)
        if int(s[i:i+2]) <= 26:
            numDecodings += self.helper(i+2,s,memo)
        
        # Cache and Return
        memo[i] = numDecodings
        return memo[i]
    
    def numDecodings(self, s: str) -> int:
        memo = {len(s):1,len(s)-1:1}
        return self.helper(0,s,memo)
