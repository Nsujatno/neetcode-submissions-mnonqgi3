# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        so basically
        im thinking recursion. for each node we recursively check the left subtree
        and then recursively check the right subtree
        """

        def validate(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        
        return validate(root, float("-inf"), float("inf"))