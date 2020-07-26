class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        results = []
        visited = [False] * n

        def solver(source, path, visited=visited):
            if source == n - 1:
                results.append(path[:])
            for i in graph[source]:
                if i not in visited:
                    visited[i] = True
                    path.append(i)
                    solver(i, path, visited)
                    path.pop()
                    visited[i] = False

        solver(0, [0], visited)
        return results