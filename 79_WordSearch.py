class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        size = len(word)
        visited = [[False]*m for i in range(n)]
        def filterutil(t):
            x = t[0]
            y = t[1]
            if x<0 or y<0 or x>=n or y>=m:
                return False
            else: return True
        def find(x,y,i):
            if i==size:
                return True
            if x<0 or y<0 or x>=n or y>=m:
                return False
            l,r,d,u = [False]*4
            dirn = filter(filterutil,[(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
            for point in dirn:
                a,b = point[0],point[1]
                if board[a][b] == word[i] and not visited[a][b]:
                    visited[a][b] = True
                    temp = find(a,b,i+1)
                    if temp: return True
                    visited[a][b] = False
            else:
                return False
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    visited[i][j] = True
                    temp = find(i,j,1)
                    if temp: return True
                visited[i][j] = False
        else:
            return False
        