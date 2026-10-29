class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        fc = [r[0] for r in matrix] + [matrix[-1][-1]]

        if target < fc[0] or target > fc[-1]:
            return False

        l, r = 0, len(fc)-1

        while r - l > 1 :

            m = l + (r-l)//2

            if fc[m] == target:

                return True

            elif fc[m] > target:
                r = m

            else:
                l = m

        fr = matrix[l]

        ul, ur = 0 , len(fr)-1

        while ul <= ur:

            m = ul + (ur-ul)//2

            if fr[m] == target:
                return True

            if fr[m] < target:
                ul = m+1
            else:
                ur = m-1

        return False