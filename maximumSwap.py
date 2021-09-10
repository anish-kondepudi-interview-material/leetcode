class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        maxVal = [0]*len(num)
        currMax = -float('inf')
        currMaxIdx = -1
        for i in range(len(num)-1,-1,-1):
            maxVal[i] = currMaxIdx
            if int(num[i]) > currMax:
                currMax = int(num[i])
                currMaxIdx = i
        
        for i in range(len(num)-1):
            if int(num[i]) < int(num[maxVal[i]]):
                return int(num[:i] + num[maxVal[i]] + num[i+1:maxVal[i]] + num[i] + num[maxVal[i]+1:])
        
        return int(num)
            
        