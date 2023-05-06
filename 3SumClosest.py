class Solution:

    def searchPartition(self, nums: List[int], partition_boundary: int, target: int) -> int:
        closest_sum = None
        min_dist = float("inf")
        l, r = 0, len(nums) - 1

        while l < r:
            # Skip over partition boundary
            if partition_boundary in (l, r):
                l += int(l == partition_boundary)
                r -= int(r == partition_boundary)
                continue

            # Updates sum
            curr_sum = nums[l] + nums[r]
            curr_dist = abs(target - curr_sum)
            if curr_dist < min_dist:
                min_dist = curr_dist
                closest_sum = curr_sum

            # Adjust pointers
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return target

        return closest_sum

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = None
        min_dist = float("inf")

        for partition_boundary, num in enumerate(nums):
            curr_closest_sum = self.searchPartition(nums, partition_boundary, target - num) + num
            curr_dist = abs(curr_closest_sum - target)
            if curr_dist < min_dist:
                closest_sum = curr_closest_sum
                min_dist = curr_dist
        
        return closest_sum
