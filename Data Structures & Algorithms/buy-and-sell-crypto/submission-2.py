class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        l,r=0,1
        while r<len(prices):
            if prices[r]>prices[l]:
                curr_prof=prices[r]-prices[l]
                maxprof=max(curr_prof,maxprof)
            else:
                l=r
            r+=1
        return maxprof