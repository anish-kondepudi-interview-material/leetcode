class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1,path2 = [],[]
        path1 = self.helper(root,p,path1)
        path2 = self.helper(root,q,path2)
        
        ans = root
        for i in range(min(len(path1),len(path2))):
            if path1[i] == path2[i]:
                ans = path1[i]
        return ans
            
        
    
    def helper(self,root,n,path):
        if root != None :
            path.append(root)
            if root == n : return path.copy()
            x = self.helper(root.left,n,path.copy())
            if x != '':
                return x
            x = self.helper(root.right,n,path.copy())
            if x != '':
                return x
        return ''