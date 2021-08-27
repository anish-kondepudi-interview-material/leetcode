class Solution:
    
    def findWater(self, left, right, arr):
        return (right-left)*min(arr[left],arr[right])
    
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        
        maxWater = 0
        while left < right:
            maxWater = max(maxWater,self.findWater(left,right,height))
            if height[left] == height[right]:
                rightInitialHeight = height[right]
                while right >= 0 and height[right] <= rightInitialHeight and right > left:
                    right -= 1
                leftInitialHeight = height[left]
                while left < len(height) and height[left] <= leftInitialHeight and right > left:
                    left += 1
            elif height[left] > height[right]:
                rightInitialHeight = height[right]
                while right >= 0 and height[right] <= rightInitialHeight and right > left:
                    right -= 1
            else:
                leftInitialHeight = height[left]
                while left < len(height) and height[left] <= leftInitialHeight and right > left:
                    left += 1
        
        return maxWater