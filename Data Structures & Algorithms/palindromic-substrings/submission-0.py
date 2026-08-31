class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s)==0:
            return 0
        
        if len(s)==1:
            return 1

        dp = list(s)

        for i in range(2,len(s)+1):

            j = 0
            while(j+i<=len(s)):
                sl = s[j:j+i]
                if sl in dp or sl == sl[::-1]:
                    dp.append(sl)
                j += 1

        return len(dp)