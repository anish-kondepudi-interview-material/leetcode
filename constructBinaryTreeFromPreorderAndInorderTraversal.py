# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, preStart, inStart, inEnd, preOrder, inOrder):
        if preStart > len(preOrder)-1 or inStart > inEnd: return None
        
        root = TreeNode(preOrder[preStart])
        
        inIdx = inOrder.index(root.val)
        
        root.left = self.construct(preStart+1, inStart, inIdx-1, preOrder,inOrder)
        root.right = self.construct(preStart+inIdx-inStart+1, inIdx+1, inEnd, preOrder, inOrder)
        
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct(0,0,len(inorder)-1,preorder,inorder)