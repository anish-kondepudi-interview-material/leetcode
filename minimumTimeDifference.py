class Solution:
    def convertMin(self, time):
        hours, minutes = map(int,time.split(":"))
        return hours*60+minutes
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Min: 0
        # Max: 1439 
        
        convertedTimes = []
        for time in timePoints:
            convertedTimes.append(self.convertMin(time))
        
        convertedTimes.sort()
        
        minTime = 1440 - (convertedTimes[-1]-convertedTimes[0])
        if minTime == 1440: minTime = 0
        for i in range(len(convertedTimes)-1):
            time1 = convertedTimes[i]
            time2 = convertedTimes[i+1]
            minTime = min(minTime,time2-time1)
        return minTime