class Solution:
    # Binary Search O(logn)
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        middle = (start+end)//2
        
        while(True):
            
            middle = (start+end)//2
            
            # Base Case #1
            if nums[middle] == target:
                return middle
            
            # Base Case #2
            if start == middle:
                if target < nums[start]:
                    return start
                if target > nums[end]:
                    return end+1
                return end
            
            if target < nums[middle]:
                end = middle
            
            if target > nums[middle]:
                start = middle
                