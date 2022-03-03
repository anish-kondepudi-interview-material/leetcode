from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        lines = defaultdict(lambda:0)
        for row in wall:
            runningSum = 0
            for i, brick in enumerate(row):
                if i == len(row)-1: break
                runningSum += brick
                lines[runningSum] += 1
        return len(wall) - (max(lines.values()) if lines else 0)
                
        
