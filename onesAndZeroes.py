class Solution:
    
    def getCounts(self, num):
        zero, one = 0, 0
        for digit in num:
            if digit == '0':
                zero += 1
            else:
                one += 1
        return (zero,one)
    
    def getSubsets(self, m, n, nums, i, counts, subsets):
        if (m,n,i) in subsets: return subsets[(m,n,i)]
        if i == len(nums): return 0
        if m+n == 0: return 0
        zeros, ones = 0, 0
        if nums[i] not in counts:
            counts[nums[i]] = self.getCounts(nums[i])
        zeros, ones = counts[nums[i]]
        consider = 0
        if m >= zeros and n >= ones:
            consider = self.getSubsets(m-zeros,n-ones,nums,i+1,counts,subsets)+1
        skip = self.getSubsets(m,n,nums,i+1,counts,subsets)
        subsets[(m,n,i)] = max(consider,skip)
        return subsets[(m,n,i)]
            
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = {}
        subsets = {}
        return self.getSubsets(m,n,strs,0,counts,subsets)