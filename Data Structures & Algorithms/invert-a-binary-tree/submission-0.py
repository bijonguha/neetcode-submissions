# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty tree or reached leaf's child
        if not root: 
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert both subtrees
        self.invertTree(root.left)   # Invert left subtree
        self.invertTree(root.right)  # Invert right subtree
        
        return root

        