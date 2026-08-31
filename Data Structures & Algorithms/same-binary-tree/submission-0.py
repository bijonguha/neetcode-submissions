# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.flag = True

        def rec(p,q):
             
            if not self.flag:
                return

            if (p and not q) or (q and not p):
                self.flag = False
            
            if not p or not q:
                return

            if (p.val != q.val):
                self.flag = False
                
            rec(p.left, q.left)
            rec(p.right, q.right)

            return
        
        rec(p,q)

        return self.flag