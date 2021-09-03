from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root,1))
        levels = {}
        while len(q) != 0:
            root, d = q.popleft()
            if root == None: continue
            if d in levels:
                levels[d].append(root.val)
            else:
                levels[d] = [root.val]
            q.append((root.left,d+1))
            q.append((root.right,d+1))
        res = list(levels.values())
        for i, level in enumerate(res):
            if i%2!=0:
                res[i] = level[::-1]
        return res        
        