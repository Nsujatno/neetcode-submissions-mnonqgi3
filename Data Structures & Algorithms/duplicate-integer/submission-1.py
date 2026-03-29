class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Create hashset, for each value if in hashset, return true
        if not in hashset, add to hashset
        at the end return false
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
