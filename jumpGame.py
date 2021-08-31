class Solution: 
    def canJump(self, nums: List[int]) -> bool:
        
        # My Solution
        # if len(nums) == 1: return True
        # steps = 0
        # for i in range(len(nums)-1):
        #     steps = max(steps,nums[i])
        #     if steps == 0:
        #         return False
        #     steps -= 1
        # return True
    
        # Better Solution (https://www.youtube.com/watch?v=Zb4eRjuPHbM)
        lastGoodIdx = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= lastGoodIdx:
                lastGoodIdx = i
        return lastGoodIdx == 0
            