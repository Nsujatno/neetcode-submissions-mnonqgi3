class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        iterate through, if the current sum becomes negative it does no help for us
        so we discard and reset a new subarray
        """
        currSum = 0
        res = nums[0]

        for num in nums:
            currSum += num
            res = max(res, currSum)
            if currSum < 0:
                currSum = 0
        
        return res
