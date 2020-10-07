from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            for j in range((len(i)+1)//2):
                i[j],i[~j] = i[~j]^1, i[j]^1
        return A