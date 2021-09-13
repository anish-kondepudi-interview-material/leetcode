class Solution:
    
    def helper(self, nums, target, res, comb, start):
        if target <= 0:
            if target == 0: res.append(comb.copy())
            return
        for i in range(start,len(nums)):
            comb.append(nums[i])
            self.helper(nums, target-nums[i], res, comb, i)
            comb.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, target, res, [], 0)
        return res