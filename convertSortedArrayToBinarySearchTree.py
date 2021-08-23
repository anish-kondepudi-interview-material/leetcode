# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreeInsertion(self, nums, start, end):
        if start > end: return None
        middle = start + (end-start)//2
        root = TreeNode(nums[middle])
        root.left = self.binaryTreeInsertion(nums, start, middle-1)
        root.right = self.binaryTreeInsertion(nums, middle+1, end)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.binaryTreeInsertion(nums, 0, len(nums)-1)
        return root