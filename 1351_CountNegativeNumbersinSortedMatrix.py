from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        li = []
        r = len(grid[0])-1
        for i in grid:
            l = 0
            if i[0]<0:
                li.append(len(i))
                total+=len(i)
                continue
            if i[-1]>0:
                li.append(0)
                continue
            while l<=r:
                mid = l+(r-l)//2
                if i[mid]<0 and i[mid-1]>=0:
                    total+=(len(i)-mid)
                    li.append((len(i)-mid))
                    break
                elif i[mid]>=0:
                    l = mid+1
                elif i[mid]<0:
                    r = mid-1
        print(li)
        return total