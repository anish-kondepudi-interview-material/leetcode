from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(lambda:0)
        for i in range(len(s)-9):
            d[s[i:i+10]] += 1
        return [k for k, v in d.items() if v > 1]
