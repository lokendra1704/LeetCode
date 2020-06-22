class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def f(s,p):
            if not p: return not s
            first_match = bool(s) and p[0] in (s[0],'.')
            if len(p)>=2 and p[1] == '*':
                return f(s,p[2:]) or first_match and f(s[1:],p)
            else:
                return first_match and f(s[1:],p[1:])
        return f(s,p)