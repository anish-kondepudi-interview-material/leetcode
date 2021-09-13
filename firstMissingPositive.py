class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Make all negative values INT_MAX
        n = len(nums)
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = float('inf')
                
        # Move values in range to start of array
        start = 0
        for num in nums:
            if num >= 1 and num <= n:
                nums[start] = num
                start += 1
        
        # Make seen indices negative
        for i in range(start):
            num = abs(nums[i])
            nums[num-1] = -abs(nums[num-1])
        
        # Check first first non-negative index
        ans = 0
        for num in nums:
            ans += 1
            if num >= 0: return ans
        return n+1