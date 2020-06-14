class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root.val
                yield from dfs(root.right)
        gen = dfs(root)
        for i in range(k):
            val = next(gen)
        return val