class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        My first thoughts is to just combine them into one string with something to indicate that that's where it splits
        The only issue is knowing what that indicator should be
        """
        res = ""
        for word in strs:
            res += word + "😊"
        return res
    def decode(self, s: str) -> List[str]:
        """
        find delimmeter and split
        """
        res = []
        i = 0
        while i < len(s):
            j = s.find("😊", i)
            if j == -1:
                break
            
            word = s[i:j]
            res.append(word)
            
            i = j + 1

        return res
