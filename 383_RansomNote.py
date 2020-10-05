class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i in a:
            if not a[i]<=b.get(i,0):
                return False
        return True