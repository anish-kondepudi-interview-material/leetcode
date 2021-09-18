class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        pairCount = {}
        for x, y in rectangles:
            ratio = y/x
            if ratio not in pairCount:
                pairCount[ratio] = 0
            pairCount[ratio] += 1
        
        ans = 0
        for value in pairCount.values():
            ans += value*(value-1)/2
        return int(ans)