class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0] 
        profit = 0
        i = 0
        sell = 0
        while (i < len(prices)):
            if (prices[i] >= current):
                if (sell < prices[i]):
                    sell = prices[i]
            else:
                temp = sell - current
                current = prices[i]
                sell = 0
                if (temp > profit):
                    profit = temp
            i += 1
        temp = sell - current
        if (temp > profit):
            profit = temp
        return profit
        