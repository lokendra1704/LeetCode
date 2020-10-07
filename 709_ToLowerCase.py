class Solution:
    def toLowerCase(self, str: str) -> str:
        l = list(str)
        for idx in range(len(l)):
            i = l[idx]
            if 65<=ord(i)<=90:
                l[idx] = chr(ord(i)+ord('a')-ord('A'))
        return ''.join(l)