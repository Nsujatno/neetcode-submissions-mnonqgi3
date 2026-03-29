class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. find the product of all non zero elements in the array
        2. for each element in output, divide product by the corresponding number in nums
        3. if there's 1 0, every other output will be 0, and the index with 0 will be the product
        4. if there's 2 0's every single number will just be 0
        """

        product = 1
        zero_counter = 0
        output = [0] * len(nums)

        # find the product of all non zero elements in nums
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_counter += 1

        if zero_counter == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = product
            return output

        if zero_counter > 1:
            return output
        
        for i in range(len(nums)):
            output[i] = product//nums[i]

        return output
