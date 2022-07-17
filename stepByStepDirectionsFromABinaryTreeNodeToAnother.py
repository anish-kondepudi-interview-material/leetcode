# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    pathToTarget = []
    
    def getPath(self, node, path, target, direction="L"):
        
        if path and path[-1][0] == target: 
            self.pathToTarget = path.copy()
            return True
        
        if node is None: 
            return False

        path.append((node.val, direction))       
        
        if self.getPath(node.left, path, target, "L"):
            return True
        if self.getPath(node.right, path, target, "R"):
            return True
        
        path.pop()
        
        return False
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        if startValue == destValue: return ""
        
        self.getPath(root, [], startValue)
        path1 = self.pathToTarget.copy()
        
        self.getPath(root, [], destValue)
        path2 = self.pathToTarget.copy()
        
        # Find idx of last common node in path1
        path2Set = set(path2)
        idxPath1 = 0
        for i, dirValNode in enumerate(path1):
            if dirValNode in path2Set:
                idxPath1 = i

        # Find idx of last common node in path2
        commonNode = path1[idxPath1]
        idxPath2 = path2.index(commonNode)
        
        # Construct path
        ans = "U"*(len(path1)-idxPath1-1)
        for i in range(idxPath2+1, len(path2)):
            ans += path2[i][1]
            
        return ans
        
        
        
        
        
        
