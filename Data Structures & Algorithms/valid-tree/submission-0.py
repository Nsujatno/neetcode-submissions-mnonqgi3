class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        # make adj list
        adj = { i:[] for i in range(n)}
        for node, neigh in edges:
            adj[node].append(neigh)
            adj[neigh].append(node)
        visited = set()


        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
