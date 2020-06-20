from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum_ = 0
        q = deque([root])
        while q:
            node = q.pop()
            if L<=node.val<=R:
                sum_+=node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return sum_