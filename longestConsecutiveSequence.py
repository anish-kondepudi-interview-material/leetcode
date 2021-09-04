class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        numsSet = set(nums)
        seen = set()
        maxLen = 0

        for num in numsSet:
            if num in seen: continue
            right = num
            left = num
            while right in numsSet:
                seen.add(right)
                right += 1
            while left in numsSet:
                seen.add(left)
                left -= 1
            maxLen = max(maxLen,right-left-1)
        return maxLen
                
            