class Solution:

    #Iterative
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root,-float("inf"),float("inf"))]
        while len(stack):
            node,lower_bound,upper_bound = stack.pop()
            
            if node.val<=lower_bound or node.val>=upper_bound:  #This is an invalid node
                return False
            if node.right:
                stack.append((node.right,node.val,upper_bound))
            if node.left:
                stack.append((node.left,lower_bound,node.val))
        return True

    ##Recursive
    def isValid(root, lower_bound=-float("inf"), upper_bound = float("inf") ):
        return not root or (lower_bound < root.val < upper_bound) and (isValid(root.left,lower_bound,root.val) and isValid(root.right, root.val, upper_bound))