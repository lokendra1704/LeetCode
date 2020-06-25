# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(inorder,preorder):
            if not inorder or not preorder: return None
            val = preorder[0]
            root = TreeNode(val)
            pos_in = inorder.index(val)
            left_inorder = inorder[:pos_in]
            last = 1 + len(left_inorder) 
            left_preorder = preorder[1:last]
            right_inorder = inorder[pos_in+1:]
            right_preorder = preorder[last:]
            root.left = helper(left_inorder,left_preorder)
            root.right = helper(right_inorder,right_preorder)
            return root
        return helper(inorder,preorder)