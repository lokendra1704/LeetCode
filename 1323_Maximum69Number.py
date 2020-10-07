class Solution:
    #98.72%
    def maximum69Number (self, num: int) -> int:
        temp = num
        i = 0
        last = -1
        while temp>0:
            if temp%10==6:
                last = i
            temp//=10
            i+=1
        return num+(3*(10**last)) if last!=-1 else num

class Solution:
    def maximum69Number (self, num: int) -> int:
        x = list(str(num))
        for i in range(len(x)):
            if x[i]=='6':
                x[i]='9'
                break
        return int(''.join(x))