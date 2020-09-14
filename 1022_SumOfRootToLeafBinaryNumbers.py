class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths,path = [],[]
        def solver(root,path):
            if not root:
                return
            path.append(root.val)
            if (root.left,root.right)==(None,None):
                paths.append(path[:])
            solver(root.left,path)
            solver(root.right,path)
            path.pop()
        solver(root,path)
        total = 0
        for i in range(len(paths)):
            paths[i] = list(map(str,paths[i]))
            paths[i] = ''.join(paths[i])
            paths[i] = int(paths[i],base=2)
            total+=paths[i]
        return total