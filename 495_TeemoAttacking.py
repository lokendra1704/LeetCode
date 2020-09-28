class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        intervals = [[i,i+duration] for i in timeSeries]
        intervals.sort()
        size = len(intervals)
        i = 1
        while i<size:
            a = intervals[i-1]
            b = intervals[i]
            if a[1]>=b[0]:
                a[1]=b[1]
                intervals.pop(i)
                size-=1
            else:
                i+=1
        return sum(i[1]-i[0] for i in intervals)