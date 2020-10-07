from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for i in range(len(arr)):
            total+= (((n-i)*(i+1)+1)//2)*arr[i]
        return total