# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def inorder(root,p = 0):
            if root:
                x = inorder(root.right,p)
                root.val += x
                y = inorder(root.left,root.val)
                if root.left:
                    return y
                else:
                    return root.val
            else:
                return p      
        inorder(root)
        return root