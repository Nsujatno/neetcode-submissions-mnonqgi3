class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2

            print(l,m,r)
            
            # look at right side
            if nums[m] > nums[r]:
                print("pop")
                l = m + 1
            # look at left side
            elif nums[m] <= nums[r]:
                print("plop")
                r = m
            
        return nums[l]