class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        
        score, maxScore = 0, 0
        left, right = 0, len(tokens)-1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                return max(maxScore, score)
                
            maxScore = max(maxScore, score)
            
        return maxScore
                
        
        
        
        
