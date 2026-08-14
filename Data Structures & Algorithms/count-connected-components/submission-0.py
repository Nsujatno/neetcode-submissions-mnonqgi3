class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}
        for node, neigh in edges:
            adj[node].append(neigh)
            adj[neigh].append(node)
        visited = set()

        def dfs(node):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        
        return res