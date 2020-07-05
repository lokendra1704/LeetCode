class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        N, M = len(image), len(image[0])
        if image[sr][sc] == newColor: return image

        def dfs(i, j, old, new=newColor):
            if 0 <= i < N and 0 <= j < M and image[i][j] == old:
                image[i][j] = new
                coord = [(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]
                for a, b in coord:
                    if 0 <= a < N and 0 <= b < M and image[a][b] == old:
                        dfs(a, b, old)

        dfs(sr, sc, image[sr][sc])
        return image