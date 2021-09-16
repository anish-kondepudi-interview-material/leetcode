class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        ans = 1
        newRangeStart, newRangeEnd = points[0]
        for start, end in points:
            if start > newRangeEnd:
                ans += 1
                newRangeStart = start
                newRangeEnd = end
            else:
                newRangeStart = max(newRangeStart, start)
                newRangeEnd = min(newRangeEnd, end)
            
        return ans