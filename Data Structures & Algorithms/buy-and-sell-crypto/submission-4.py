class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 0
        max_price = 0
        end_price = 0
        for i in range(0, len(prices)):
            if i < len(prices) -1 and prices[start] < prices[i + 1]:
                end = i + 1
                end_price = max(end_price, prices[end])
            else:
                max_price = max(max_price, end_price - prices[start])
                start = i + 1
                end = i + 1
                end_price = 0
        return max_price
        
        