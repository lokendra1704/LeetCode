class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = -1
        if not strs: return ""
        minlength = float("inf")
        for i in strs:
            if len(i) < minlength:
                minlength = len(i)
        while prefix < minlength - 1:
            letter = strs[0][prefix + 1]
            for i in strs:
                if i[prefix + 1] != letter:
                    return i[:prefix + 1]
            else:
                prefix += 1
        return strs[0][:prefix + 1]


x = Solution().longestCommonPrefix(["flower","flow","flight"])
print(x)