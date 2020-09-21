class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.n = len(nums)
        n= self.n
        tree = [0]*(2*n)
        tree[n:2*n] = nums[:]
        for i in range(n-1,0,-1):
            tree[i] = tree[2*i]+tree[2*i+1]
        self.tree = tree
        
    def update(self, i: int, val: int) -> None:
        i+=self.n
        self.tree[i]=val
        while i>0:
            l,r = i,i
            if i%2==0:
                r=i+1
            else:
                l=i-1
            self.tree[i//2] = self.tree[l]+self.tree[r]
            i//=2

    def sumRange(self, i: int, j: int) -> int:
        total = 0
        i+=self.n
        j+=self.n
        while i<=j:
            if i%2==1:
                total+=self.tree[i]
                i+=1
            if j%2==0:
                total+=self.tree[j]
                j-=1
            i//=2
            j//=2
        return total
