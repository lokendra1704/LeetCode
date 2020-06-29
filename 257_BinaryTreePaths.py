class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, res, path):
            if root.left == None and root.right == None:
                res.append(path)
            if root.left != None:
                dfs(root.left, res, path + '->' + str(root.left.val))
            if root.right != None:
                dfs(root.right, res, path + '->' + str(root.right.val))

        if not root:
            return []
        res = []
        dfs(root, res, '' + str(root.val))
        return res


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        result = []

        def solver(temp, s):
            if not temp.left and not temp.right:
                if not s:
                    s = str(temp.val)
                else:
                    s += "->" + str(temp.val)
                result.append(s)
            if not s:
                s = str(temp.val)
            else:
                s += "->" + str(temp.val)
            if temp.left: solver(temp.left, s)
            if temp.right: solver(temp.right, s)

        solver(root, "")
        return result


class Solution:
    def binaryTreePaths(self, R: TreeNode) -> List[str]:
        A, P = [], []
        def dfs(N):
            if N == None: return
            P.append(N.val)
            if (N.left, N.right) == (None, None):
                A.append('->'.join(map(str, P)))
            else:
                dfs(N.left)
                dfs(N.right)
            P.pop()

        dfs(R)
        return A