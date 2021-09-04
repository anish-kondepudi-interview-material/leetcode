class Solution:
    def isPalindrome(self,s):
        return s == s[::-1] 
    
    def all_partitions(self, string):
        # Stole implementation (Can do myself = check solution tab on leetcode)
        for cutpoints in range(1 << (len(string)-1)):
            result = []
            lastcut = 0
            for i in range(len(string)-1):
                if (1<<i) & cutpoints != 0:
                    result.append(string[lastcut:(i+1)])
                    lastcut = i+1 
            result.append(string[lastcut:])
            yield result

    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        res = []
        for partition in self.all_partitions(s):
            isValid = True
            for substr in partition:
                if substr not in memo.keys():
                    memo[substr] = self.isPalindrome(substr)
                if not memo[substr]:
                    isValid = False
            if isValid:
                res.append(partition)
        return res
            
        