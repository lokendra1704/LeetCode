class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = start
        for i in range(1,n):
            l^=(start + 2*i)
        return l