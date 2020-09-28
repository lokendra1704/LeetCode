class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1,m+1)]
        result = []
        for i in queries:
            result.append(arr.index(i))
            arr.insert(0,arr.pop(result[-1]))
        return result