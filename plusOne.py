class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        endIdx = len(digits)-1
        while endIdx >= 0:
            if digits[endIdx] < 9:
                digits[endIdx] += 1
                return digits
            else:
                digits[endIdx] = 0
                endIdx -= 1
        digits.insert(0,1)
        return digits
        