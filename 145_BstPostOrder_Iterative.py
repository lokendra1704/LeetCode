# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        s = deque([(root,False)])
        ans = []
        while s:
            node,visited = s.pop()
            if visited:
                ans.append(node.val)
            else:
                s.append((node,True))
                if node.right: s.append((node.right,False))
                if node.left: s.append((node.left, False))
        return ans