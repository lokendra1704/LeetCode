class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        d = Counter(secret)
        l = [False]*len(guess)
        for i in range(len(guess)):
            if guess[i]==secret[i]:
                d[guess[i]]-=1
                bulls+=1
                l[i] = True
        for i in range(len(guess)):
            if not l[i] and d.get(guess[i],0)>0:
                d[guess[i]]-=1
                cows+=1
        return f'{bulls}A{cows}B'