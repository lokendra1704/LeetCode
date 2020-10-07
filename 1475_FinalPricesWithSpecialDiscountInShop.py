from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)-1,-1,-1):
            temp = prices[i]
            while stack:
                if stack[-1]<=temp:
                    prices[i]-=stack[-1]
                    break
                else:
                    stack.pop()
            stack.append(temp)
        return prices