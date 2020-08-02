class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = num
            total = 0
            while temp > 0:
                total += temp % 10
                temp //= 10
            num = total
        return num