class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        max_profit = 0
        for i in range(1, len(prices)):
            if (prices[p2] < prices[p1]):
                p1 = p2
            else:
                max_profit = max(prices[p2] - prices[p1], max_profit)
            p2 += 1
        return max_profit
            
        
        