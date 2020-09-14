from collections import Counter
class Solution:
    def partitionLabels(self, S):
        c = Counter(S)
        result = []
        i,j=0,0
        d={}
        while j<len(S) and i<len(S):
            d[S[j]] = d.get(S[j],0) + 1
            c[S[j]] = c.get(S[j],0) - 1
            ans = True
            for k in d:
                ans = ans and (c[k]==0)
            if ans:
                result.append(j-i+1)
                i=j+1
                j=i
            else:
                j+=1
        return result

    def abc(self, S):
        if not S:
            return False
        result = []
        d = {b:a for a,b in enumerate(S)}
        j = 0
        anchor = 0
        for i in range(len(S)):
            j = max(j,d[S[i]])
            if i==j:
                result.append(i-anchor+1)
                anchor = i+1
        return result

print(Solution().abc("ababcbacadefegdehijhklij"))