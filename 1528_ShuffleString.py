class Solution:
    def restoreString(self, s, indices):
        l = list(s)
        for i in range(len(indices)):
            while indices[i]!=i:
                a = indices[i]
                l[i],l[a] = l[a],l[i]
                indices[i],indices[a] = indices[a],indices[i]
        return ''.join(l)

x = Solution().restoreString("codeleet",[4,5,6,7,0,2,1,3])