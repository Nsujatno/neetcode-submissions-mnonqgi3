class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        # initialize countT hashmap
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have and need counters
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            # add to window hashmap
            window[c] = 1 + window.get(c, 0)

            # does window[c] satisft the condition in countT[c]
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # loop until condition false
            while have == need:
                # update res
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left
                window[s[l]] -= 1

                # if the character we just removed is part of the character that we need
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""