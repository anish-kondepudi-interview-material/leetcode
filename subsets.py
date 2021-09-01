class Solution:
    
    def helper(self, nums, sub_res, res):
        if len(nums) == 0:
            return
        for i, num in enumerate(nums):
            tmp_res = sub_res.copy()
            tmp_res.append(num)
            res.append(tmp_res)
            self.helper(nums[i+1:],tmp_res,res)
           
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.helper(nums,[],res)
        return res
        