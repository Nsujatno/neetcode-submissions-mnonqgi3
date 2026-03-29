class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need a hash map with the number and the frequency
        # for every number in the array, update hashmap
        final = []
        hashmap = defaultdict(int)
        for i in range(0, len(nums)):
            hashmap[nums[i]] += 1
        pairs = list(hashmap.items())
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        print(sorted_pairs)
        for i in range(0, k):
            final.append(sorted_pairs[i][0])
        return final