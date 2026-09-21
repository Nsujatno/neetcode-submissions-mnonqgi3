class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        take product of every value
        divide by each index's value for that value
        if there is one 0, the index of that is the product and everything else is 0
        if there is two 0's, everything is 0
        """
        product, zero_counter, zero_index = 1, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
                zero_index = i
            else:
                product *= nums[i]

        res = [0 for _ in range(len(nums))]
        if zero_counter >= 2:
            return res
        elif zero_counter == 1:
            res[zero_index] = product
            return res
        else:
            for i in range(len(nums)):
                res[i] = product // nums[i]
            return res
