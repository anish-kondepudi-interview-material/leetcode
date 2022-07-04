from collections import defaultdict

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = defaultdict(lambda: 0)
        for word in words1:
            d1[word] += 1
            
        d2 = defaultdict(lambda: 0)
        for word in words2:
            d2[word] += 1
        
        count = 0
        for c1, cnt1 in d1.items():
            if cnt1 == 1 and d2[c1] == 1:
                count += 1
                
        return count
