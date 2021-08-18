# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSame(root1, root2):
            if root1 != None and root2 == None or root1 == None and root2 != None:
                return False
            if root1 == None and root2 == None:
                return True
            if root1.val != root2.val:
                return False
            return (isSame(root1.left, root2.left) and isSame(root1.right,root2.right))
        
        return isSame(p,q)