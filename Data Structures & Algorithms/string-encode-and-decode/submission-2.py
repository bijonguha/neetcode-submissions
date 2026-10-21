class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        st = "".join([str(len(j))+"#"+j for j in strs])
        return st

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []

        strs = []
        a = []
        i = 0

        while i < len(s):

            if s[i] != "#":
                a.append(s[i])
                i += 1
            else:
                n = int("".join(a))
                a = []
                strs.append(s[i+1:i+n+1])
                i = i+1+n

        return strs
                
