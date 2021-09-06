class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            mask = {}
            inUse = set()
            isValid = True
            for char1, char2 in zip(pattern,word):
                if char1 in mask.keys():
                    if mask[char1] != char2:
                        isValid = False
                        break
                else:
                    if char2 in inUse:
                        isValid = False
                        break
                    mask[char1] = char2
                    inUse.add(char2)
            if isValid:
                res.append(word)
        return res
                    