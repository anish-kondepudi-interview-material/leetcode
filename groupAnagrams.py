class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        
        for word in strs:
            
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1
                
            count = tuple(count)
            
            if count in table.keys():
                table[count].append(word)
            else:
                table[count] = [word]
                
        return table.values()
                