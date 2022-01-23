# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        
        # Put Nodes into Array
        currNode = head
        while currNode:
            nodes.append(currNode)
            currNode = currNode.next
            
        # Change Pointers To 0 -> N -> 1 -> N-1 -> 2 -> N-2 ...
        for i in range(len(nodes)//2):
            nodes[i].next = nodes[len(nodes)-1-i]
            nodes[len(nodes)-1-i].next = nodes[i+1]
        nodes[(len(nodes)//2)].next = None
    
        return head
            
        
