class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        hashmap = {}
        res = 0

        for r in range(len(s)):
            char = s[r]
            hashmap[char] = 1 + hashmap.get(char, 0)

            while (r - l + 1) - max(hashmap.values()) > k:
                # decrement the left one from the hashmap
                hashmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res