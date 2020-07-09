from collections import defaultdict
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        R,C = len(M),len(M[0])
        #graph
        bonds = defaultdict(list)
        for r in range(R):
            for c in range(C):
                if M[r][c]:
                    bonds[r].append(c)       
        if not bonds: return 0
        #Check for no connected components
        def dfs(graph,source,visited):
            for i in graph[source]:
                if not visited[i]:
                    visited[i]=True
                    dfs(graph,i,visited)
        groups = 0
        visited = [False]*len(bonds)
        for i in bonds:
            if not visited[i]:
                dfs(bonds,i,visited)
                groups+=1
                
        return groups
                    
                