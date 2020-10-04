from collections import defaultdict
class Solution:
    def findCircleNum(self, M):
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
            visited[source]=True
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

#Solution Using DisjointSetUnion (Union Find)
class Solution1:
    def findCircleNum(self, M):
        f = {i:i for i in range(len(M))}
        def find(n):
            if n!=f[n]:
                f[n] = find(f[n])
            return f[n]
        def union(a,b):
            f[find(a)] = find(b)
            
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] and i!=j:
                    union(i,j)
        return sum(find(i)==i for i in range(len(M)))
                    
x = Solution1().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
print(x)