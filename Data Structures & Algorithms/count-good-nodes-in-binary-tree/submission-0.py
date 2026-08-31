# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        par_val = 0
        flag = True
        li = []
        tl = []

        def helper(root, up_val, flag, tl):
            tmp_tl = tl.copy()
            tmp_tl.append(up_val)
            
            if not root:
                return

            if flag == True:
                if root.val >= up_val:
                    flag = True
                    li.append(root.val)
                else:
                    flag = False

            if flag == False:
                if root.val >= max(tmp_tl):
                    flag = True
                    li.append(root.val)
            
            up_val = root.val
            tmp_tl.append(root.val)

            helper(root.left, up_val, flag, tmp_tl)
            helper(root.right, up_val, flag, tmp_tl)

        helper(root, float('-inf'), True, tl)

        print(li)
        return len(li)
