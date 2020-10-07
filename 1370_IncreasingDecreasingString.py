from collections import Counter
from string import ascii_lowercase
class Solution:
    def sortString(self, s: str) -> str:
        l = ""
        c = Counter(s)
        limit = len(s)
        while limit>0:
            for k in range(ord('a'),ord('z')+1):
                i=chr(k)
                if c.get(i,0)>0:
                    l+=i
                    c[i]-=1
                    limit-=1
            for k in range(ord('z'),ord('a')-1,-1):
                i=chr(k)
                if c.get(i,0)>0:
                    l+=i
                    c[i]-=1
                    limit-=1
        return l

#Written Elegant
def sortString(self, s: str) -> str:
        cnt, ans, asc = Counter(s), [], True
        while cnt:                                                                  # if Counter not empty.
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):   # traverse keys in ascending/descending order.
                ans.append(c)                                                       # append the key.
                cnt[c] -= 1                                                         # decrease the count.
                if cnt[c] == 0:                                                     # if the count reaches to 0.
                    del cnt[c]                                                      # remove the key from the Counter.
            asc = not asc                                                           # change the direction, same as asc ^= True.
        return ''.join(ans)

#More Pythonic Way
def sortString(self, s: str) -> str:
    counter, result = Counter(s), []
    while counter:
        for traverse in ascii_lowercase, reversed(ascii_lowercase):
            result += [c for c in traverse if c in counter]
            counter -= dict.fromkeys(counter, 1)
    return ''.join(result)