# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        queue = deque()
        queue.append(root)
        vals = []
        while len(queue) != 0:
            node = queue.popleft()
            if node:
                vals.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append("None")
        return ",".join(vals)
            
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "None": return None
        
        orderQueue = deque(data.split(','))
        nodesQueue = deque()
        
        root = TreeNode(orderQueue.popleft())
        nodesQueue.append(root)
        
        while len(orderQueue) != 0:
            node = nodesQueue.popleft()
            val1 = orderQueue.popleft()
            if val1 != "None":
                node.left = TreeNode(val1)
                nodesQueue.append(node.left)
            val2 = orderQueue.popleft()
            if val2 != "None":
                node.right = TreeNode(val2)
                nodesQueue.append(node.right)
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
