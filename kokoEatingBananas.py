class Solution:
    
    def isValidK(self, piles, k, h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/k)
            if hours > h: return False
        return hours <= h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r-l)//2
            if self.isValidK(piles, m, h):
                k = m
                r = m-1
            else:
                l = m+1

        return k

    
    