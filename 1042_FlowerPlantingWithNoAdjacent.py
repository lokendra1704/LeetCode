#85.81%
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N, paths):
        graph = defaultdict(list)
        for i in paths:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        color = []
        for i in range(1,N+1):
            choice = [1, 2, 3, 4]
            for k in graph[i]:
                try:
                    choice.remove(color[k-1])
                except:
                    pass
            color.append(choice[0])
        return color


#66.94%
from collections import defaultdict, deque
class Solution:
    def gardenNoAdj(self, N, paths):
        if not paths and not N:
            return []
        color = [1] * N
        if not paths and N:
            return color
        graph = defaultdict(list)
        for i in paths:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        visited = {}
        def explore(source, color=color, visited=visited):
            q = deque([source])
            visited[source] = True
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    choice = [1, 2, 3, 4]
                    for k in graph[node]:
                        try:
                            choice.remove(color[k - 1])
                        except:
                            pass
                        if k not in visited:
                            visited[k] = True
                            q.append(k)
                    color[node - 1] = choice[0]
        for i in graph:
            if i not in visited:
                explore(i)
        return color

x = Solution().gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]])
print(x)