class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        max_price = 0
        array_length = len(prices)
        if (len(prices) < 2):
            return 0
        while p2 < array_length:
            if (prices[p1] > prices[p2]):
                p1 = p2
                p2 += 1
            else:
                max_price = max(max_price, prices[p2] - prices[p1])
                p2 += 1

        return max_price

        