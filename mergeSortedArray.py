class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return

        endIdx = len(nums1)-1
        m -= 1
        n -= 1
        
        while m >= 0 and n >= 0:
            
            if nums1[m] >= nums2[n]:
                nums1[endIdx] = nums1[m]
                m -= 1
            else:
                nums1[endIdx] = nums2[n]
                n -= 1
                
            endIdx -= 1
            
        if n >= 0:
            for i in range(n+1):
                nums1[i] = nums2[i]
        