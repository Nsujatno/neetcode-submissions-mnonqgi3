class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Sliding window, where you want the highest val after the curr min value
        So we should start with left, right = 0, 1
        Iterate through the array, keeping track of a curr min at the left pointer
        if right pointer is less, then set left pointer = to the right pointer, and iterate right pointer
        """
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            # check if val at right pointer is less than
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
        return profit
