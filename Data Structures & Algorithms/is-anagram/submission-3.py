class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = {}

        for i,j in zip(s,t):
            count[i] = count.get(i,0) + 1
            count[j] = count.get(j,0) - 1
        
        return all(num == 0 for num in list(count.values()))