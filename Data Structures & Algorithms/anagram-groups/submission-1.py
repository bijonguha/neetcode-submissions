from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            c = [0]*26

            for i in s:
                n = ord(i)-ord('a')
                c[n]+=1
            
            d[str(c)].append(s)
        
        return list(d.values())
        