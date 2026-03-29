class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
                print(f"profit is {profit}")
            else:
                left = right
            right += 1
        return profit 