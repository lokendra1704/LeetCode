#Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root: return 0
        def dfs_in(root,total=0):
            if not root.left and not root.right:
                if total+root.val==s:
                    return True
                else:
                    return False
            if root:
                a,b = False,False
                if root.left:
                    a = dfs_in(root.left,root.val+total)
                if root.right:
                    b = dfs_in(root.right,root.val+total)
                return a or b
        return dfs_in(root)

#Iterative
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root: return False
        stack = deque([(root,0)])
        while stack:
            node,total = stack.pop()
            if not node.left and not node.right and total+node.val==s:
                return True
            if node.left:
                stack.append((node.left,total+node.val))
            if node.right:
                stack.append((node.right,total+node.val))
        return False