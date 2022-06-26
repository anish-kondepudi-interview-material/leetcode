class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
#         [1,2,3,4,5] = pushed
#         [4,5,3,2,1] = popped
        
#         - if you cant pop, then push
#         - if you can pop, then do it
        
#         []
#         [1]
#         [1,2]
#         [1,2,3]
#         [1,2,3,4]
#         [1,2,3]
#         [1,2,3,5]
#         [1,2,3]
#         [1,2]
#         [1]
#         []
        
        pushedIdx, poppedIdx = 0, 0
        stack = []
        while poppedIdx < len(popped):
            if pushedIdx < len(pushed) and (len(stack) == 0 or stack[-1] != popped[poppedIdx]):
                stack.append(pushed[pushedIdx])
                pushedIdx += 1
            elif stack[-1] == popped[poppedIdx]:
                stack.pop()
                poppedIdx += 1
            else:
                return False
        return True
        
        
        
