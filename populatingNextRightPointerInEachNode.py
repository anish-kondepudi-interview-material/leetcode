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
    # My Solution O(N) time and O(N) space - multiple passes
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
        
    # Better O(N) time and O(1) Space Solution (Not Mine)
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return None 

#         curr = root 

#         while curr.left is not None:
#             next_level = curr.left 

#             while curr is not None:
#                 curr.left.next = curr.right 

#                 if curr.next is None:
#                     curr.right.next = None 
#                 else:
#                     curr.right.next = curr.next.left 

#                 curr = curr.next 

#             curr = next_level 

#         return root 
        
        