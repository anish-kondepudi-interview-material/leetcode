from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rSet = {}
        self.rArr = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.rSet.keys(): return False
        
        addIdx = len(self.rArr)
        self.rArr.append(val)
        self.rSet[val] = addIdx
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.rSet.keys(): return False
        
        delIdx = self.rSet[val]
        lastIdx = len(self.rArr)-1
        self.rArr[delIdx], self.rArr[lastIdx] = self.rArr[lastIdx], self.rArr[delIdx]
        self.rArr.pop()
        del self.rSet[val]
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randIdx = randint(0,len(self.rArr)-1)
        return self.rArr[randIdx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()