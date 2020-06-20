from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = deque([root])
        result = []
        while q:
            node = q.pop()
            result.append(node.val)
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return result