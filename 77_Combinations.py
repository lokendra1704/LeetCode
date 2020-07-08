class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(s,seen,res,start):
            if len(res)==k:
                results.append(res[:])
            for j in range(start,len(s)):
                i = s[j]
                if i not in seen:
                    res.append(i)
                    seen.add(i)
                    dfs(s,seen,res, j)
                    res.pop()
                    seen.remove(i)
        seen = set()
        s = [i for i in range(1,n+1)]
        res=[]
        results = []
        dfs(s,seen,res,0)
        return results