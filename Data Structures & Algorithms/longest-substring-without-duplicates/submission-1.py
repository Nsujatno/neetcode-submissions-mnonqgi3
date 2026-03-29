class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, left and right pointers
        # if val at right pointer not in hash set, add to hash set and iterate right pointer
        # if val at right pointer is in the hash set, move left pointer until it is no longer in set
        hash = set()
        left = 0
        right = 0
        length = 0
        while right < len(s) and left <= right:
            if s[right] not in hash:
                hash.add(s[right])
                # print(f"{s[right]} added to hashset")
                right += 1
            else:
                while(s[right] in hash):
                    hash.remove(s[left])
                    # print(f"{s[left]} removed from hashset")
                    left += 1
            length = max(length, right - left)
        # print(f"right: {right} and left: {left}")
        return length
