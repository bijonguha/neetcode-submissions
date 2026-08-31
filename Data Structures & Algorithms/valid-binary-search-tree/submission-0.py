# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function for DFS, with value boundaries
        def dfs(node, low, high):
            if not node:
                return True
            # Value must be strictly between low and high
            if not (low < node.val < high):
                return False
            # Left subtree: value < node.val
            # Right subtree: value > node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        # Initial boundaries: (-infinity, +infinity)
        return dfs(root, float('-inf'), float('inf'))
