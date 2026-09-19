class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        ts = sorted(t)
        if ss == ts:
            return True
        else:
            return False