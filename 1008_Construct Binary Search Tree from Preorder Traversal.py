#BEST SOLUTION
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1,len(preorder)):
            n = TreeNode(preorder[i])
            if len(stack) > 0:
                if stack[-1].val > n.val:
                    stack[-1].left = n
                else:
                    tn = None
                    while len(stack) > 0 and stack[-1].val < n.val:
                        tn = stack.pop()
                    tn.right = n
            stack.append(n)
        return root

##Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return []
        head = TreeNode(preorder.pop(0))
        for val in preorder:
            node=TreeNode(val) 
            #insert(head,node)
            cur = (head,0)
            prev = None
            while cur[0]:
                prev = cur
                if val < cur[0].val:
                    cur = (cur[0].left,-1)
                else:
                    cur = (cur[0].right,1)
            if cur[1]==1:
                prev[0].right = node
            else:
                prev[0].left = node
        return head


#Recursive
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return []
        def insert(head,node):
            val = node.val
            if val<head.val:
                if head.left:
                    insert(head.left,node)
                else:
                    head.left = node
            if val>head.val:
                if head.right:
                    insert(head.right,node)
                else:
                    head.right = node
        head = TreeNode(preorder.pop(0))
        for val in preorder:
            node=TreeNode(val) 
            insert(head,node)
        return head