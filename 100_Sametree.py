class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def solver(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            else:
                return p.val == q.val and solver(p.left, q.left) and solver(
                    p.right, q.right)

        return solver(p, q)
