class Solution:
    def rotate(self, m):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        for i in range(n//2):
            for j in range(i,n-i-1):
                m[j][~i],m[~i][~j],m[~j][i],m[i][j] = \
                m[i][j],m[j][~i],m[~i][~j],m[~j][i]

mat = [[1,2,3],[4,5,6],[7,8,9]]  
for i in mat:
    print(i)      
Solution().rotate(mat)
print('------------')
for i in mat:
    print(i)