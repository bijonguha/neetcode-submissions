class Solution:

    def encode(self, strs: List[str]) -> str:
    
        sc = "#"
    
        strs = [f"{len(i)}#{i}" for i in strs]

        return "".join(strs)

    def decode(self, s: str) -> List[str]:
    
        sl = []

        while len(s) > 0:
            ind = s.index("#")
            si = int(s[:ind])
            sis = s[ind+1:ind+si+1]
            sl.append(sis)
            s = s[ind+si+1:]

        return sl