# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([(root,0)])
        maxwidth = 1
        while q:
            l,r = q[0][1],q[-1][1]
            maxwidth = max(maxwidth, r-l+1)
            for i in range(len(q)):
                node,idx = q.popleft()
                if node.left: q.append((node.left,2*idx+1))
                if node.right: q.append((node.right,2*idx+2))
            
        return maxwidth
        