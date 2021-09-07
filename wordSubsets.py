class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        masterSubset = {}
        
        for word in words2:
            
            tempSubset = {}
            
            # Create tempSubset
            for char in word:
                if char in tempSubset.keys():
                    tempSubset[char] += 1
                else:
                    tempSubset[char] = 1
                    
            # Update masterSubset with tempSubset data
            for key in tempSubset.keys():
                if key not in masterSubset.keys() or masterSubset[key] < tempSubset[key]:
                    masterSubset[key] = tempSubset[key]
        
        res = []
        
        for word in words1:
            subset = masterSubset.copy()
            
            # Remove subset values from subset
            for char in word:
                if char in subset.keys():
                    subset[char] -= 1
            
            # Check if subset values are valid
            isValid = True
            for value in subset.values():
                if value > 0:
                    isValid = False
                    break
            if isValid: res.append(word)

        return res
            
            
        
        
        
                
        