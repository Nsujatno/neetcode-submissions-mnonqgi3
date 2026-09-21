class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucket sort
        where the index of the array = the frequency
        the value at that index is a list of the numbers that appear that many times.
        """
        occurences = {}
        # get hashmap of number, occurences
        for num in nums:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1
        
        # go from hashmap to array that we described
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in occurences.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        