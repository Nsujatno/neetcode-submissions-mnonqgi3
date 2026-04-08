class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        we use dynamic programming and basically add up the stuff
        so we have a new msb at 1,2,4, etc the powers of 2. which we need to keep track of
        if new msb
        else then you do 1 + dp[n-msb]
        """
        msb = 1

        # answers
        ans = []

        for i in range(n+1):
            # for the first one
            if i == 0:
                ans.append(0)
                continue
            
            # for the first 1
            if i == 1:
                ans.append(1)
                continue

            # if power of 2
            if i == msb * 2:
                msb = msb * 2
                ans.append(1)
            else:
                ans.append(1 + ans[i - msb])

        return ans

                
            