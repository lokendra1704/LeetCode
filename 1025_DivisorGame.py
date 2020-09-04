class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False]*(N+1)
        for i in range(N+1):
            for j in range(1,N):
                if not i%j and not dp[i-j]:
                    dp[i] = True
        return dp[N]