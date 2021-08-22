class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIdx = 0
        for num in nums:
            if num != 0:
                nums[nonZeroIdx] = num
                nonZeroIdx += 1
        for i in range(nonZeroIdx,len(nums)):
            nums[i] = 0
        