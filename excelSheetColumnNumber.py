class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        delta = 1
        i = len(columnTitle)-1
        while i >= 0:
            total += delta*(ord(columnTitle[i])-ord('A')+1)
            delta *= 26
            i -= 1
        return total
        