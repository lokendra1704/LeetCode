class Solution:
    def minTimeToVisitAllPoints(self, points):
        if not points:
            return 0
        total = 0
        sx,sy = points[0][0],points[0][1]
        for i in range(1,len(points)):
            a,b = points[i][0],points[i][1]
            while not sx==a or not sy==b:
                if a>sx:
                    sx+=1
                elif a<sx:
                    sx-=1
                if b>sy:
                    sy+=1
                elif b<sy:
                    sy-=1
                total+=1
        return total
                
print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))