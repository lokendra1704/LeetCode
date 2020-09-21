#Speed 96.49%
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.ans = 0
        def solver(i,j,dx,dy):
            if i==len(board) or i<0 or j<0 or j==len(board[0]) or board[i][j]=='B':
                return
            if board[i][j]=='p':
                self.ans+=1
                return
            solver(i+dx,j+dy,dx,dy)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='R':
                    solver(i,j,0,1)
                    solver(i,j,1,0)
                    solver(i,j,-1,0)
                    solver(i,j,0,-1)
        return self.ans