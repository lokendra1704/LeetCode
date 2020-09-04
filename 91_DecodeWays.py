class Solution:
    def numDecodings(self, s):
        if not s or s[0]=='0':
            return 0
        dp = [0]*(len(s)+1)
        dp[0],dp[1] = 1,1
        for j in range(2,len(s)+1):
            i = j-1
            if 0<int(i)<10:
                dp[j]=dp[j-1]
            if s[i-1]!='0' and 0<int(s[i-1:i+1])<27:
                dp[j]+=dp[j-2]
        return dp[-1]