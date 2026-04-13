class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = max_price = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                max_price = max(max_price, prices[r] - prices[l])
                r += 1
        return max_price

        
        