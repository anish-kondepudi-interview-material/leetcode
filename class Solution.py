class Solution:
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        for i, num in enumerate(nums):
            ans += '0' if num[i] == '1' else '1'
        return ans
    
#     def helper(self, s, depth, res):
#         if len(s) == depth:
#             res.append(s)
#             return
#         self.helper(s+'0', depth, res)
#         self.helper(s+'1', depth, res)
    
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         res = []
#         self.helper('',len(nums[0]), res)
        
#         numsSet = set(nums)
#         for num in res:
#             if num not in numsSet:
#                 return num
#         return