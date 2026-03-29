# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Solving this with dfs, we need to call this function recursively
        Typical dfs works like (in order)
        - recursivecall(curr.left)
        - action
        - recursivecall(curr.right)

        we just do the same thing but the action is swapping the nodes
        our stopping point is when 
        """
        if root is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root
