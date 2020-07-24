class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        results = []
        zigzag = False
        while q:
            level = deque()
            for i in range(len(q)):
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                if zigzag:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
            zigzag=~zigzag
            results.append(level)
        return results