class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = set(J)
        return sum(i in d for i in S)