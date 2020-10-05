class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        mx = 0
        mncost = float("inf")
        for i in range(0,n):
            if prices[i]<mncost:
                mncost = prices[i]
            else:
                temp = prices[i]-mncost
                if temp>mx:
                    mx = temp
        return mx