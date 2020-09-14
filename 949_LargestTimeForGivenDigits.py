class Solution:
    def largestTimeFromDigits(self, A):
        n = len(A)
        t = sum(A)
        mx = ""
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or i==k:
                        continue
                    else:
                        hh = str(A[i])+str(A[j])
                        mm = str(A[k])+str(t-A[i]-A[j]-A[k])
                        time = hh+":"+mm
                        if hh<"24" and mm<"60" and time>mx:
                            mx = time
        return mx