# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root,l):
            if root:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
        l1=[]
        l2 = []
        inorder(root1,l1)
        inorder(root2,l2)
        l1.extend(l2)
        l1.sort()
        return l1