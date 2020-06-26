class Solution:
    @staticmethod
    def solve(str):
        d = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
        num = 0
        str = list(str)
        sign = None
        i=0
        while True:
            if not str: break
            if str[i]=='-':
                sign = -1
                str.pop(i)
                break
            elif str[i]=='+':
                sign=1
                str.pop(i)
                break
            elif str[i] in d:
                sign = 1
                break
            else:
                str.pop(i)
            #i+=1
        
        for i in str:
            if i not in d:
                continue
            else:
                num = num*10 + d[i]
        return num*sign
x = Solution.solve("    -42")
print(x,type(x))