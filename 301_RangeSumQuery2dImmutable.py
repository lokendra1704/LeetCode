from itertools import accumulate
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.plr = [list(accumulate(i)) for i in matrix]
        self.pud = list(zip(*[list(accumulate(i)) for i in zip(*matrix)]))

    def sumRegion(self, a: int, b: int, c: int, d: int) -> int:
        plr,pud = self.plr,self.pud
        ans = 0
        for i in range(b,d+1):
            ans+=pud[c][i]
            if a>0:
                ans-=pud[a-1][i]
        for i in range(a,c+1):
            ans+=plr[i][d]
            if b>0:
                ans-=plr[i][b-1]
        return ans//2


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)