# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        so basically,
        can i not just uh. traverse the tree, store every element in an array
        sort the array
        then select the kth-1 node?
        ima try dat
        """
        nodes = []
        
        def dfs(node):
            if not node:
                return
            
            nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        nodes.sort()
        return nodes[k-1]