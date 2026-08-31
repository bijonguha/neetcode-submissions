class Solution:
    def isPalindrome(self, s: str) -> bool:

      if len(s) <= 1:
        return True

      import re
      s_n = re.sub(r'[^A-Za-z0-9]', '', s)
      s_f = s_n.replace(" ","")
      s_f = s_f.lower()

      if len(s_f)%2 == 0:

        piv = int(len(s_f)/2)
        ls = s_f[ : piv]
        rs = s_f[piv : ][::-1]

        if ls == rs:
          return True

      else:

        piv = int(len(s_f)/2)
        ls = s_f[ : piv]
        rs = s_f[piv+1 : ][::-1]

        if ls == rs:
          return True

      return False