class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = list(S)

        def dfs(s, i):
            if len(s) == len(S):
                result.append(''.join(s))
            else:
                if S[i].isalpha():
                    dfs(s + S[i].swapcase(), i + 1)
                dfs(s + S[i], i + 1)

        result = []
        dfs("", 0)
        return result