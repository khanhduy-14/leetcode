# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(q.right, p.right)
        def dfs(root):
            if not root:
                return False
            if root.val == subRoot.val and isSameTree(root, subRoot):
                    return True
            if dfs(root.left):
                return True
            if dfs(root.right):
                return True
            return False

        return dfs(root)