class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        res = []
        
        def helper(node, level):
            if not node:
                return
            
            # If we've gone deeper than current result, add a new list
            if level == len(res):
                res.append([])
            
            # Add current node's value to its level list
            res[level].append(node.val)
            
            # Recurse left and right children with level+1
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        helper(root, 0)
        res_new = [r[-1] for r in res]
        return res_new

        