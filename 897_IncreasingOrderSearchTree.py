from collections import deque
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = deque()
        def dfs(node,l):
            if not node:return
            if node.left: dfs(node.left,l)
            l.append(node)
            if node.right: dfs(node.right,l)
        dfs(root,l)
        head = cur = l.popleft()
        while l:
            cur.left=None
            cur.right = l.popleft()
            cur = cur.right
        return head


from collections import deque
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.val
                yield from dfs(node.right)
        ans = cur = TreeNode(None)
        for v in dfs(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

from collections import deque
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                dfs(node.right)
        ans = self.cur = TreeNode(None)
        dfs(root)
        return ans.right