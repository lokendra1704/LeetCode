class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path= []
        result = []
        candidates.sort()
        def backtrack(i,path,total):
            if total==target and path not in result:
                result.append(path[:])
                return
            if total>target:
                return
            for j in range(i,len(candidates)):
                path.append(candidates[j])
                backtrack(j+1,path,total+candidates[j])
                path.pop()
        backtrack(0,path,0)
        return result