class Solution:
    
    def helper(self, s, start, sub_res, res):

        # Base Case (If you have 4 numbers and used all of string)
        if len(sub_res) == 4:
            if start == len(s): res.append(sub_res.copy())
            return
        
        # Add number and recurse
        end = start
        for i in range(1,4):
            
            # Edge case (going out of bounds)
            if end+i > len(s): break
            num = s[start:end+i]
            
            # Edge case (leading zeros and greater than 255)
            if num[0] == '0' and len(num) > 1: break
            if int(num) > 255: break
            
            sub_res.append(num)
            self.helper(s, end+i, sub_res, res)            
            sub_res.pop()
            
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Find all valid IPs
        res = []
        self.helper(s,0,[],res)
        
        # Convert IP Lists to Strings with Delimiter of "."
        ans = []
        for li in res:
            ans.append(".".join(li))
        
        return ans
