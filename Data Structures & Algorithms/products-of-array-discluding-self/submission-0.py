class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. multiply all the non zero numbers together
        2. for each index divide the product by nums[i]
        3. if there's 1 0, then every number besides that will be 0
        4. if there's 2 0's, then every number will be 0
        """
        product = 1
        zero_counter = 0
        output = [0] * len(nums)
        for num in nums:
            if num == 0:
                zero_counter += 1
            else:
                product *= num
        
        # check for 0s and such
        if zero_counter == 1:
            # set every other index besides the 0 one to 0.
            for i in range(len(output)):
                if nums[i] != 0:
                    output[i] = 0
                else:
                    output[i] = product
            return output

        if zero_counter > 1:
            return output 

        # if no 0's
        for i in range(len(output)):
            output[i] = product//nums[i]

        print(product)

        return output