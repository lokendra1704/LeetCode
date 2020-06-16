# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, TreeNode(
            -float("inf"))

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if not self.first and (self.prev.val > root.val):
                self.first = self.prev
            if self.first and self.prev.val > root.val:
                self.second = root

            self.prev = root
            inorder(root.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
