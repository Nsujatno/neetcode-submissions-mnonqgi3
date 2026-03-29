class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointers solution where you check if sum > target, move right pointer
        if sum < target move left pointer
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            print(numbers[l], numbers[r])
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1