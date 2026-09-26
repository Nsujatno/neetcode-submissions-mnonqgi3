class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1