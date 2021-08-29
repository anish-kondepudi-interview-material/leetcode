class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Edge Cases (Array size 0 and 1)
        if len(nums) == 0: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        
        maxArr1 = nums[-1]
        minArr2 = nums[0]
        
        inArr1 = (target <= maxArr1)
        inArr2 = (target >= minArr2)
        isSorted = (nums[0] < nums[-1])
        
        # Edge Cases (At border of rotation)
        if not inArr1 and not inArr2: return -1
        if target == maxArr1: return len(nums)-1
        if target == minArr2: return 0
        
        # Binary Search (Modified for rotated sorted array)
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if not isSorted:
                if inArr1:
                    if nums[middle] >= minArr2:
                        left = middle+1
                        continue
                if inArr2:
                    if nums[middle] <= maxArr1:
                        right = middle-1
                        continue
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
            else:
                left = middle+1
                
        return -1