class Solution:
    # O(n) Solution
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # 2 Pointer Solution
        
        ptr1 = 0
        ptr2 = len(nums) - 1
        
        if len(nums) == 0: return 0
        
        while ptr1 <= ptr2:
            if nums[ptr1] == val:
                while nums[ptr2] == val:
                    if ptr2 == ptr1:
                        return ptr1
                    ptr2 -= 1
                nums[ptr1] = nums[ptr2]
                ptr2 -= 1
            ptr1 += 1
        
        return ptr1
    
    # Move to start Solution (Not Mine, but really like the simplicity of this solution)
    
    c=0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[c],nums[i]=nums[i],nums[c]
            c+=1
    return c
            
                
        
        
        
        