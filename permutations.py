class Solution:
    
    def helper(self, nums, sub_res, res):
        if len(nums)==1:
            sub_res.append(nums[0])
            res.append(sub_res)
            return
        for i in range(len(nums)):
            temp = nums.copy()
            temp2 = sub_res.copy()
            temp2.append(temp.pop(i))
            self.helper(temp,temp2,res)
        return
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0: return [[]]
        if len(nums)==1: return [nums]
        
        res = []
        self.helper(nums,[],res)
        return res
    
    # My Solution is Above O(n*n!) Time and O(n^2) space
    # Better Solution https://www.youtube.com/watch?v=s7AvT7cGdSo&t=519s