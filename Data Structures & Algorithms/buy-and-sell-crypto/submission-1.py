class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                prof=prices[j] - prices[i]
                maxprof=max(maxprof,prof)
        return maxprof