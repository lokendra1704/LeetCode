from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = deque([root])
        length = 0
        while q:
            length+=1
            for i in range(len(q)):
                node = q.popleft()
                if node: q.extend(node.children)
        return length