class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We need hashmap and find if the target - curr val is in the hashmap, if it is retunr curr index
        and the index of that value

        so if the reciprocal isnt found, we store into hashmap as a key value pair of number and index
        """

        hashmap = {}
        for i in range(0, len(nums)):
            curr_val = nums[i]
            reciprocal = target - curr_val
            if reciprocal in hashmap:
                return [hashmap[reciprocal], i]

            # add to hashmap
            hashmap[curr_val] = i