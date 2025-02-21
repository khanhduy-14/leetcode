# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.set = set()
        root.val = 0
        self.set.add(root.val)
        self.preorder(root)


    def find(self, target: int) -> bool:
        if target not in self.set:
            return False
        return True


    def preorder(self, root: Optional[TreeNode]):
        if root.left:
            root.left.val = 2 * root.val + 1
            self.set.add(2 * root.val + 1)
            self.preorder(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.set.add(2 * root.val + 2)
            self.preorder(root.right)
        


        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)