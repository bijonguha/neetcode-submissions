class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if s == t:
            return True

        if self.hash_set(s) == self.hash_set(t):
            return True
        else:
            return False

    def hash_set(self, ar):

        d = {}

        for i in ar:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        return d
