class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        arrSum = sum(nums)
        
        tempSum = 0
        for i, num in enumerate(nums):
            tempSum += i*num
        
        maxSum = tempSum
        for i in range(len(nums)):
            tempSum += (nums[i]*len(nums)-arrSum)
            maxSum = max(maxSum, tempSum)
            
        return maxSum