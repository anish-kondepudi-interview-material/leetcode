class Solution:
    
    # Shift Character O(1)
    def shift(self, char, shifts):
        return str(chr((((ord(char)-ord('a'))+shifts)%26)+ord('a')))
        
    # Shift Word O(N)
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        # Sum up shifts O(N)
        prev = 0
        for i in reversed(range(len(shifts))):
            shifts[i] += prev
            prev = shifts[i]
        
        # Append shifted char to result O(N)
        res = ''
        for i in range(len(shifts)):
            res += self.shift(s[i],shifts[i])
        return res