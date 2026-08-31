# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return -1  # return -1 so that a leaf's height is 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # calculate diameter “through” this node: left + right + 2 edges, but since we count edges, not nodes, we just add left_height + right_height + 2
            current_diameter = left_height + right_height + 2
            
            self.max_diameter = max(self.max_diameter, current_diameter)
            # return height to parent call (edges below this node)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter  # since at least one node, and the diameter is in edges
        