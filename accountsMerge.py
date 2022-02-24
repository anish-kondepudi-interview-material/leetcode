from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountsMap = defaultdict(list)
        for account in accounts:
            accountsMap[account[0]].append(set(account[1:]))
        
        for accountSets in accountsMap.values():
            i = 0
            n = len(accountSets)
            while i < n:
                currSet = accountSets[i]
                while True:
                    removeIdx = []
                    m = len(accountSets)
                    for j in range(i+1,m):
                        newSet = accountSets[j]
                        for email in newSet:
                            if email in currSet:
                                currSet = currSet.union(newSet)
                                removeIdx.append(j)
                                break
                    accountSets[i] = currSet
                    for idx in reversed(removeIdx):
                        accountSets.pop(idx)
                    if m == len(accountSets): break
                i += 1
                n = len(accountSets)
        
        res = []
        for accountName, accountSets in accountsMap.items():
            for accountSet in accountSets:
                res.append([accountName]+sorted(list(accountSet)))
        
        return res
