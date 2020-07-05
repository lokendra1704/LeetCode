class Solution:
    def islandPerimeter(self, image):
        N, M = len(image), len(image[0])
        self.peri = 0
        self.seen = set()

        def dfs(i, j):
            if 0 <= i < N and 0 <= j < M and image[i][j] == 1:
                self.seen.add((i, j))
                coord = [(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]
                for a, b in coord:
                    n = (a,b)
                    if (a, b) not in self.seen:
                        dfs(a, b)
            else:
                self.peri += 1

        for i in range(N):
            for j in range(M):
                if image[i][j] == 1:
                    dfs(i, j)
                    return self.peri


x = Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0],
                                [1, 1, 0, 0]])
print(x)