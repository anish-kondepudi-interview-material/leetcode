class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(nlogn)
        # Space: O(1)
        # return sorted(s) == sorted(t)
    
        # Time: O(N)
        # Space: O(N)
        seen = {}
        for c in s:
            if c in seen.keys():
                seen[c] += 1
            else:
                seen[c] = 1
        for c in t:
            if c in seen.keys():
                seen[c] -= 1
            else:
                return False
        for value in seen.values():
            if value != 0:
                return False
        return True
        