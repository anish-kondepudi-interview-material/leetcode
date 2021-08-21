# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # Taking advantage of Node.val constraints
        # O(A+B) time; O(1) Space
        currNode = headA
        while currNode:
            currNode.val += 100000
            currNode = currNode.next
        
        connectionNode = None
        currNode = headB
        while currNode:
            if currNode.val > 100000:
                connectionNode = currNode
                break
            currNode = currNode.next
            
        currNode = headA
        while currNode:
            currNode.val -= 100000
            currNode = currNode.next
        
        return connectionNode
    
        ##Traverse both heads. Then shift forward one head to intersection is approached at same time
        ##O(A+B) time; O(1) space
        ##Not my solution
        #curr1, curr2 = headA,headB
        #
        ##once any of the two pointers reach the end then move other pointer head such that both heads 
        ##will be at same distance from intersection
        #while curr1 or curr2:
        #  if curr1: curr1 = curr1.next
        #  else: headB = headB.next
        #  if curr2: curr2 = curr2.next
        #  else: headA = headA.next
        #
        ##find the intersection point when it becomes equal
        #while headA is not headB:
        #    headA = headA.next
        #    headB = headB.next
        #
         #return headA
    
        # Using Sets
        # O(A+B) time; O(A+B) space
        # s = set()
        # while headA:
        #     s.add(id(headA))
        #     headA = headA.next
        # while headB:
        #     if id(headB) in s:
        #         return headB
        #     headB = headB.next
        # return None
        