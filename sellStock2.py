class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        buyPrice = prices[0]
        prevPrice = prices[0]
        
        for price in prices:
            if price < prevPrice:
                profit += prevPrice - buyPrice
                buyPrice = price
            prevPrice = price
            
        profit += (prevPrice-buyPrice)
        
        return profit
                