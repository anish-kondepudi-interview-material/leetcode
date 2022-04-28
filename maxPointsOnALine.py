from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # Edge Case
        if len(points) <= 2: return len(points)
        
        maxPts = -1
        
        # Check for Horizontal and Slanted Lines
        for x1, y1 in points:
            d = defaultdict(lambda: 1)
            for x2, y2 in points:
                if x1 == x2: continue
                
                m = (y2-y1)/(x2-x1) if x2 > x1 else (y1-y2)/(x1-x2)
                b = y1-m*x1
                
                d[(m,b)] += 1
                
            if d: maxPts = max(maxPts, max(d.values()))
                
        # Check for Vertical Lines
        d = defaultdict(lambda: 0)
        for x, y in points:
            d[x] += 1
        maxPts = max(maxPts, max(d.values()))
        
        return maxPts
