# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        From before we checked if two trees are equal
        We want to check whether the subroot is equal to any of the subtrees of root
        So we traverse the tree and check if root.val = subroot.val, check if the trees are equal at that point
        """
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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
    