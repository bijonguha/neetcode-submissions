# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, count):

            if not root:
                return 0

            count += 1
            
            count = max(count, dfs(root.left, count), dfs(root.right, count))

            return count

        count = dfs(root, 0)

        return count