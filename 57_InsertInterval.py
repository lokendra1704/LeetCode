class Solution:
    def insert(self, intervals,newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        l = []
        l.append(intervals.pop(0))
        if intervals:
            for i in intervals:
                a = l[-1]
                b = i
                if a[1]>=b[0] and a[1]<=b[1]:
                    l[-1] = [a[0],b[1]]
                elif a[1]>=b[0] and a[1]>b[1]:
                    continue
                else:
                    l.append(i)
        return l

print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))