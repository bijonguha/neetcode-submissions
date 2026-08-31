class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

      m = len(matrix)
      n = len(matrix[0])

      m_ar = [a[0] for a in matrix]

      ml, mr = 0, len(m_ar)-1

      while ml<=mr:

        mm = (ml+mr)//2

        if target > m_ar[mm]:
          ml+=1
        elif target < m_ar[mm]:
          mr-=1
        else:
          return True

      mmat = min(ml,mr)

      print(f"mid index found {mmat}")

      n_ar = matrix[mmat]

      nl, nr = 0, len(n_ar)-1

      while nl<=nr:

        nm = (nl+nr)//2

        if target > n_ar[nm]:
          nl+=1
        elif target < n_ar[nm]:
          nr-=1
        else:
          return True
      return False
         