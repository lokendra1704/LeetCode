class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x))[2:]
        y = str(bin(y))[2:]
        mxln = max(len(x),len(y))
        x = x.rjust(mxln,"0")
        y = y.rjust(mxln,"0")
        return sum([bool(a!=b) for a,b in zip(x,y)])
        