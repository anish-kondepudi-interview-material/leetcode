# Not my solution - but very clean explanation
# Only continue to check subportion in which characters are equal
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/discuss/1367217/O(MN)-easy-to-understand
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        def inOrder(s, ind):
            res = []
            for i in ind:
                if s[i] < s[i+1]:
                    continue
                elif s[i] > s[i+1]:
                    return False, []
                else:
                    res.append(i)
            return True, res
        count = 0
        ind = [i for i in range(m-1)]
        for i in range(n):
            newStrs = [s[i] for s in strs]
            b, res = inOrder(newStrs, ind)
            if not b:
                count += 1
            elif res:
                ind = res
            else:
                return count
        return count