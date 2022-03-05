from collections import defaultdict
class Solution:
    
    def findMaxPts(self, idx, nums, memo):
        if idx >= len(nums):
            return 0
        if idx == len(nums)-1:
            return nums[idx][0]*nums[idx][1]
        if idx in memo:
            return memo[idx]
        
        maxPts = -float('inf')
        num, count = nums[idx]
        numNext = nums[idx+1][0]
        
        if num+1 == numNext:
            maxPts = max(maxPts, num*count+self.findMaxPts(idx+2, nums, memo))
        
        if num+1 < numNext:
            maxPts = max(maxPts, num*count+self.findMaxPts(idx+1, nums, memo))
        
        maxPts = max(maxPts, self.findMaxPts(idx+1, nums, memo))
        
        memo[idx] = maxPts
        return maxPts
            
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        numsMap = defaultdict(lambda: 0)
        for num in nums:
            numsMap[num] += 1
        
        numsCount = sorted([(k,v) for k,v in numsMap.items()])
        return self.findMaxPts(0, numsCount, {})
        
        
