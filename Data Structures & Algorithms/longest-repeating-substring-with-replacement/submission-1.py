class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            hashmap[char] = 1 + hashmap.get(char, 0)

            if (r - l + 1) - max(hashmap.values()) <= k:
                res = max(res, r - l + 1)
            else:
                while (r - l + 1) - max(hashmap.values()) > k:
                    hashmap[s[l]] -= 1
                    l += 1
        
        return res