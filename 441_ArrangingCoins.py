class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            cur = k * (k + 1) // 2
            if cur == n:
                return k
            elif cur > n:
                right = k - 1
            else:
                left = k + 1
        return right