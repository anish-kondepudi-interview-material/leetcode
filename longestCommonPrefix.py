class Solution:  
    # O(N*M) Time Complexity where N is length of shortest string and M is number of strings
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        answer = ''
    
        # Find first and last string (sorted alphabetically)
        firstString = min(strs)
        lastString = max(strs)
        
        for i in range(len(firstString)):
            if firstString[i] == lastString[i]:
                answer += firstString[i]
            else:
                break
        
        return answer