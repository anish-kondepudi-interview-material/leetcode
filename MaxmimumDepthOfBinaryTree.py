# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getMaxDepth(root):
            if root is None:
                return 0
            return max(getMaxDepth(root.left),getMaxDepth(root.right))+1
        
        return getMaxDepth(root)