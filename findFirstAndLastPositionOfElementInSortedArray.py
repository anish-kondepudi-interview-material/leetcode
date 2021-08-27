class Solution:
    
    def expand(self, nums, idx):
        target = nums[idx]
        left = idx
        right = idx
        while True:
            if left-1 >= 0 and nums[left-1] == target:
                left -= 1
            else:
                break
        while True:
            if right+1<len(nums) and nums[right+1] == target:
                right += 1
            else:
                break
        return [left,right]
    
    def binarySearch(self, left, right, target, nums):
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle+1
        return -1
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        idx = self.binarySearch(0,len(nums)-1,target,nums)
        return [-1,-1] if idx==-1 else self.expand(nums,idx)
        