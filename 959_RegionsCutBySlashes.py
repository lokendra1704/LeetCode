class DSU:
    def __init__(self,size):
        if size>0:
            self.id = [i for i in range(size)]
            self.size = [1]*size
            self.numberOfComponents = size

    def find(self,p):
        root = p
        while self.id[root]!=root:
            root = self.id[root]

        #path-compression
        while p!=root:
            _next = self.id[p]
            self.id[p] = root
            p = _next

        return root

    def connected(self,x,y):
        return self.find(x)==self.find(y)

    def componentSize(self,x):
        return self.size[self.find(x)]

    def components(self):
        return self.numberOfComponents

    def union(self,x,y):
        a = self.find(x)
        b = self.find(y)
        if a==b:
            return
        if self.size[a] > self.size[b]:
            self.id[b] = a
            self.size[a]+=self.size[b]
        else:
            self.id[a] = b
            self.size[b]+=self.size[a]
        self.numberOfComponents-=1

class Solution:
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(N*N*4)
        for r,row in enumerate(grid):
            #if '\\' in grid[r]:
                #grid[r].replace('\\','\ ')
            for c,val in enumerate(row):
                root = 4*(r*N+c)
                if val in '/ ':
                    dsu.union(root,root+1)
                    dsu.union(root+2,root+3)
                if val in '\ ':
                    dsu.union(root+2,root)
                    dsu.union(root+1,root+3)
            
                #North-south
                if r+1<N: dsu.union(root+3,root+N*4)
                if r-1>=0: dsu.union(root,root-4*N+3)
                    
                #East-west
                if c+1<N: dsu.union(root+2,root+4+1)
                if c-1>=0: dsu.union(root+1,root-4+2)
                    
        return dsu.components()
        