class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if(len(prices)<=1): return 0
        
        maxRange = -1
        min = prices[0]
        
        for price in prices:
            if (price - min > maxRange): maxRange = price - min
            if (price < min): min = price
        
        return maxRange
            