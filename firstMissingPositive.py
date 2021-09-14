class Solution:
    
    # SOLUTION 1
    def swap(self, nums, i):
        # If already in place (don't swap)
        if nums[i] == i+1: return False
        
        # Swap Values if in range
        if nums[i] >= 1 and nums[i] <= len(nums):
            # If already in place, don't swap - else swap
            if nums[nums[i]-1] == nums[i]: return False
            num = nums[i]
            nums[i], nums[num-1] = nums[num-1], nums[i]
            return True
        else:
            return False
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            if not self.swap(nums, i):
                i += 1
                
        i = 0
        while i < len(nums):
            if nums[i] != i+1: return i+1
            i += 1
        return len(nums)+1
            
        
#     # Solution 2     
#     def firstMissingPositive(self, nums: List[int]) -> int:
        
#         # Make all negative values INT_MAX
#         n = len(nums)
#         for i, num in enumerate(nums):
#             if num < 0:
#                 nums[i] = float('inf')
                
#         # Move values in range to start of array
#         start = 0
#         for num in nums:
#             if num >= 1 and num <= n:
#                 nums[start] = num
#                 start += 1
        
#         # Make seen indices negative
#         for i in range(start):
#             num = abs(nums[i])
#             nums[num-1] = -abs(nums[num-1])
        
#         # Check first first non-negative index
#         ans = 0
#         for num in nums:
#             ans += 1
#             if num >= 0: return ans
#         return n+1