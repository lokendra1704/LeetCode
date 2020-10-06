class Solution:
    def oddCells(self, n, m, indices):
        r = [0]*n
        c = [0]*m
        for a,b in indices:
            r[a]^=1
            c[b]^=1
        return sum((i+j)&1 for j in c for i in r)