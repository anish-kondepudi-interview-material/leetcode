class Solution:
    
    def smallestLargerElement(self, nums, minimum, start, end):
        res = float('inf')
        resIdx = -1
        for i in range(start,end):
            if nums[i] > minimum and nums[i] < res:
                res = nums[i]
                resIdx = i
        return (res, resIdx)
                
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-2,-1):
            el, idx = self.smallestLargerElement(nums, nums[i+1], i+2, len(nums))
            if idx == -1: continue
            nums[i+1], nums[idx] = nums[idx], nums[i+1]
            nums[i+2:] = sorted(nums[i+2:])
            return
        nums.reverse()
            
                