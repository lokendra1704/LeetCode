class Solution:
    def combinationSum(self, candidates, target):
        def solver(start, end, path, target):
            if target == 0:
                results.append(path[:])
            elif target > 0:
                for i in range(start,end):
                    path.append(candidates[i])
                    solver(i, end, path, target - candidates[i])
                    path.pop()

        results = []
        solver(0, len(candidates), [], target)
        return results

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        def backtrack(i,path,total):
            if total==target:
                result.append(path[:])
                return
            if total>target:
                return
            for j in range(i,len(candidates)):
                path.append(candidates[j])
                backtrack(j,path,total+candidates[j])
                path.pop()
        backtrack(0,path,0)
        return result