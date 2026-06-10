"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        we want to store a hashmap of the ones weve visited and as we process link it up
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)

            # add it to hashmap
            oldToNew[node] = copy

            # do dfs on neighbors
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        
        return dfs(node) if node else None
