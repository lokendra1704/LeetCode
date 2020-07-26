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