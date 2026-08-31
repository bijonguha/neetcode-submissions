class Solution:
    @classmethod
    def groupAnagrams(self, strs):

        def listtodict(ar):

            d_ar = {}

            for i in range(len(ar)):

                if ar[i] in d_ar:
                    d_ar[ar[i]].append(i)

                else:
                    d_ar[ar[i]] = [i]

            return d_ar 

        ar = [str(sorted(i)) for i in strs]

        s_ar = listtodict(ar)

        res = []

        for k,v in s_ar.items():
            res.append([strs[i] for i in v])

        return res