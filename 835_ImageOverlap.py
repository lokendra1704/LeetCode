class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        r = len(A)
        c = len(A[0])
        def overlap(A,B):
            ans = -float("inf")
            for x in range(r):
                for y in range(c):
                    temp = 0
                    for i in range(x,r):
                        for j in range(y,c):
                            if A[i][j] and B[i-x][j-y]:
                                temp+=1
                    ans = max(temp,ans)
            return ans
        return max(overlap(A,B),overlap(B,A))