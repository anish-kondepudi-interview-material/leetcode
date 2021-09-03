"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        q.append(root)
        
        while len(q) != 0:
            if q[0] is None: break
            level = []
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                level.append(node)
                q.append(node.left)
                q.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root
                
        
        