# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        DFS through the tree and check if values are the same
        """
        # if they are both null
        if not p and not q:
            return True
        # if one is null and the other isn't
        if not p or not q:
            return False
        # if the values are diff
        if not(p.val == q.val):
            return False
        # check if both left and right return true
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

