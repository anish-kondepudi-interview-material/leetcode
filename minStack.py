class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        val = self.mainStack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
        return val
        

    def top(self) -> int:
        return self.mainStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()