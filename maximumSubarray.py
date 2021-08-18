class Solution:
    # O(n) solution
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's Algorithms
        # Either start new sum add to previous
        # And then continuously update the max
        # https://www.youtube.com/watch?v=jnoVtCKECmQ
        
        currSum = nums[0]
        maxSum = nums[0]
        
        for i, num in enumerate(nums):
            if i == 0: continue
            currSum = max(currSum+num,num)
            maxSum = max(maxSum,currSum)
        
        return maxSum
            
                
            
            
            
        