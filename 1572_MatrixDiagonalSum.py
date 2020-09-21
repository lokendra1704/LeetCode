class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        t = sum(mat[i][i]+mat[i][~i] for i in range(len(mat)))
        return t-mat[len(mat)//2][len(mat)//2] if len(mat)%2 else t