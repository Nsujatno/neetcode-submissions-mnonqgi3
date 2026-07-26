class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        sort and then check if +1 and record current length
        """
        nums.sort()
        print(nums)
        res = 1
        answer = 0
        if not nums:
            return 0
        seq = nums[0]
        for i in range (1, len(nums)):
            # if it is part of the consecutive sequence
            if nums[i] == seq + 1:
                # add 1 to the output
                res += 1
            elif nums[i] == seq:
                continue
            else:
                # reset res
                answer = max(res, answer)
                res = 1
            # update seq
            seq = nums[i]
        return max(answer, res)
