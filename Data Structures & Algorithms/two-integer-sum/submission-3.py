class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reciprocals = {}
        for i in range (len(nums)):
            reciprocal = target - nums[i]
            if reciprocal in reciprocals:
                return [reciprocals[reciprocal], i]
            else:
                reciprocals[nums[i]] = i