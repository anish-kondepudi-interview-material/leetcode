class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        prevInterval = intervals[0]
        for i, interval in enumerate(intervals):
            if interval[0] <= prevInterval[1] and interval[1] >= prevInterval[1]:
                prevInterval[1] = interval[1]
            elif interval[0] > prevInterval[1]:
                res.append(prevInterval)
                prevInterval = interval
            if i == len(intervals)-1:
                res.append(prevInterval)
        return res
    
        # Cleaner solution here (same time complexity)
        # https://leetcode.com/problems/merge-intervals/solution/