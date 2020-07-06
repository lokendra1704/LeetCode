class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        i = size-1
        carry = 1
        while i>=0:
            digits[i]= digits[i]+carry
            carry = digits[i]//10
            digits[i]%=10
            if not carry: break
            if i==0 and carry:
                digits.insert(0,carry)
                break
            i-=1
        return digits