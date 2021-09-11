class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2: return nums.index(max(nums))
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            m = l + (r-l)//2
            if m == len(nums)-1:
                return m
            elif m == 0:
                return nums.index(max([nums[0],nums[1]]))
            elif nums[m-1] < nums[m] and nums[m] < nums[m+1]:
                l = m+1
            elif nums[m-1] > nums[m] and nums[m] > nums[m+1]:
                r = m-1
            elif nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            else:
                r = m-1
        
        return m