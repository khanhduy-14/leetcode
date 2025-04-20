# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                res=False
                return 0
            return 1 + max(left, right)
        dfs(root)
        return res