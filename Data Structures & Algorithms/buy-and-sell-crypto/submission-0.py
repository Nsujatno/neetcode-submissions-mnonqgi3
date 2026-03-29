class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit.append(prices[j] - prices[i])
        if len(profit) == 0:
            return 0
        profit.sort()
        return profit[len(profit) - 1]