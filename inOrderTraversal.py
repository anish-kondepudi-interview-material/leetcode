# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def printInOrder(root, li):
            if root == None: return
            printInOrder(root.left,li)
            li.append(root.val)
            printInOrder(root.right,li)
            return li
        
        li = []
        return printInOrder(root, li)
            
            
        