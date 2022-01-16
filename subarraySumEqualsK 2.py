class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        sumCount = {0:1}
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum-k in sumCount:
                result += sumCount[currSum-k]
            if currSum not in sumCount:
                sumCount[currSum] = 0
            sumCount[currSum] += 1
        return result