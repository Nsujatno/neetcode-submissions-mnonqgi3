class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        so basically,
        to avoid duplicated we sort our solution and we test every possible a value, skipping any duplicate a's
        then we just do two sum on the rest of our solution using two pointers approach
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # do two sum on the rest of the array
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1

        return res
            