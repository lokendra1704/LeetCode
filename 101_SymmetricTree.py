# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        q = deque([root])
        while q:
            result = []
            for i in range(len(q)):
                node = q.popleft()
                if node: result.append(node.val)
                else: result.append("null")
                if node:
                    q.append(node.left)
                    q.append(node.right)
            for i in range(len(result)//2):
                if result[i]!=result[~i]:
                    return False
        return True
        