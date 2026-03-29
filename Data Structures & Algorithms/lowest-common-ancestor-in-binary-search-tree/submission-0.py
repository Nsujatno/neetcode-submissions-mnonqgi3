# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        so bst means at a node n, the left subtree is less than n and the right subtree
        is greater than n

        so at n, if both p and q are less than n, move to left subtree
        if both p and q are greater than n, move to right subtree
        else, that means n is the LCA
        """
        # base case
        if not root or not p or not q:
            return None
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root





