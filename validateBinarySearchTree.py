# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isInOrder = True
    currVal = -float("inf")
    
    def inOrder(self, root):
        if root is None: return
        self.inOrder(root.left)
        if root.val > self.currVal: 
            self.currVal = root.val
        else:
            self.isInOrder = False
        self.inOrder(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.currVal = -float("inf")
        self.isInOrder = True
        self.inOrder(root)
        return self.isInOrder
        
        