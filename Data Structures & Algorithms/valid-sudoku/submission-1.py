class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            l1,l2 = [],[]
            [l1.append(n) for n in board[i] if n != "."]
            [l2.append(m) for m in [b[i] for b in board] if m != "."]

            if len(l2) != len(set(l2)) or len(l1) != len(set(l1)):
                return False
        
        for i in range(3):
            for j in range(3):
                l3 = [b[j*3:3*(j+1)] for b in board[i*3:3*(i+1)]]
                l3 = [i for i in l3[0]+l3[1]+l3[2] if i != "."]
                if len(l3) != len(list(set(l3))):
                    return False
        
        return True
                
