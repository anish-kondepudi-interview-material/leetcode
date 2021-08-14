# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        startNode = ListNode()
        tailNode = startNode
        
        if not l1: return l2
        elif not l2: return l1
        
        while l1 and l2:
            if l1.val <= l2.val:
                tailNode.next = l1
                tailNode = tailNode.next
                l1 = l1.next
            else:
                tailNode.next = l2
                tailNode = tailNode.next
                l2 = l2.next
        
        if l1 and not l2:
            tailNode.next = l1
        elif l2 and not l1:
            tailNode.next = l2
        
        return startNode.next
        
            
                