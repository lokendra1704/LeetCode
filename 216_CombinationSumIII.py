class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results,path = [],[]
        def solver(path,total,start=0):
            if len(path)>k:
                return
            if total==0 and len(path)==k:
                results.append(path[:])
            else:
                for i in range(start+1,10):
                    if i not in path:
                        path.append(i)
                        solver(path,total-i,i)
                        path.pop()
        solver([],n)
        return results