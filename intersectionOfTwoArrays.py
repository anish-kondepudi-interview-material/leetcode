class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        for num in nums1:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        for num in nums2:
            if num in count.keys() and count[num] > 0:
                count[num] -= 1
                result.append(num)
        return result
        