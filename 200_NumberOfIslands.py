class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.n = len(grid)
        if self.n:
            self.m = len(grid[0])
        else: return 0
        def dfs(i,j):
            if not 0<=i<self.n or not 0<=j<self.m or grid[i][j]=="0":
                return
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count