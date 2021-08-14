class Solution:
    # O(n) solution
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ptr = 0
        prevNum = -101
        
        for num in nums:
            if num > prevNum:
                nums[ptr] = num
                ptr += 1
                prevNum = num
        
        return ptr
            
        