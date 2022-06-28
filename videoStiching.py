class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clips.sort(key=lambda x: x[0])
        
        maxIdx = 0
        maxReachIdx = 0
        count = 0
        
        res = []

        i = 0
        while True:
            currI = i
            while i < len(clips) and clips[i][0] <= maxIdx:
                if clips[i][1] > clips[maxReachIdx][1]:
                    maxReachIdx = i
                i += 1
            if i == currI:
                return -1
            count += 1
            maxIdx = clips[maxReachIdx][1]
            if i >= len(clips) or clips[maxReachIdx][1] >= time: break
            
        
        return count if clips[maxReachIdx][1] >= time else -1
        
