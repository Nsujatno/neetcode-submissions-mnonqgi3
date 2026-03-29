class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def rob(i):
            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(rob(i+1), nums[i] + rob(i+2))
            return memo[i]

        return rob(0)
