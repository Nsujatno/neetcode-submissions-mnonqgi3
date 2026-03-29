# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS, uses a queue
        The important here thing is the level, we want to be able to basically take a snapshot
        of how many values 
        """
        if not root:
            return []

        output = []

        # create queue
        queue = [(root)]

        # bfs
        while queue:
            level = []
            
            size = len(queue)
            # print(f"size is {size}")

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                # print(node.val)
                # print(f"level is {level}")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level)
        return output
