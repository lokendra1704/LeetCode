class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        wasneg = 1
        if x < 0:
            wasneg = -1
            x = abs(x)
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        valid = 2**31
        if num > valid:
            return 0
        return num * wasneg
